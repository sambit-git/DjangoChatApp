from django import forms

class MessageForm(forms.Form):
    message = forms.CharField( widget=forms.TextInput(attrs={ 'id' : 'msg', 'autocomplete' : 'off', 'placeholder' : 'Type your message here', 'autofocus':'autofocus' }), label='')