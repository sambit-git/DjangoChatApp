import asyncio, json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        thread_obj = await self.get_thread(me, other_user)
        self.thread = thread_obj
        chat_room = f"thread_{thread_obj.id}"
        self.chat_room = chat_room
        # await asyncio.sleep(10)

        await self.channel_layer.group_add(
            chat_room, self.channel_name
        )

        await self.send({
            "type" : 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Receive", event)
        form_data = event.get("text", None)
        if form_data is not None:
            form_dict_data = json.loads(form_data)
            msg = form_dict_data.get("message")
            user = self.scope['user']
            my_response = {
                "message"   : msg,
                "user"      : user.username
            }
            if user.is_authenticated:
                await self.save_message(self.thread, user, msg)
                await self.channel_layer.group_send(
                    self.chat_room, 
                    {
                        "type" : "chat_message",
                        "text" : json.dumps(my_response)
                    }
                )

    async def chat_message(self,event):
        print(event['text'])
        await self.send(
            {
                "type" : "websocket.send",
                "text" : event['text']
            }
        )
    async def websocket_disconnect(self, event):
        print("Disconnected", event)

    @database_sync_to_async
    def get_thread(self, user, other_user):
        return Thread.objects.get_or_new(user, other_user)[0]
    
    @database_sync_to_async
    def save_message(self, thread, user, msg):
        ChatMessage.objects.create(thread = thread, user = user, message = msg)