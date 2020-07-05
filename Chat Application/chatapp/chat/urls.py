from django.urls import path
from .views import ThreadView, InboxView

app_name = 'chat'

urlpatterns = [
    path('', InboxView.as_view(), name='home'),
    path('<str:username>/', ThreadView.as_view(), name='chat')
]