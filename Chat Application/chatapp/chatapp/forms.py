from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label = "", widget = forms.TextInput(attrs={"class" : "form-control input_user", 'placeholder' : 'xyz@example.com'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class" : "form-control input_pass", 'placeholder' : 'password'}), label = "")

class RegistrationForm(forms.Form):
    username = forms.CharField(label = "", widget = forms.TextInput(attrs={"class" : "form-control input_user", 'placeholder' : 'username'}))
    email = forms.CharField(label = "", widget = forms.EmailInput(attrs={"class" : "form-control input_user", 'placeholder' : 'xyz@example.com'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class" : "form-control input_pass", 'placeholder' : 'password'}), label = "")
    confirmpassword = forms.CharField(widget = forms.PasswordInput(attrs={"class" : "form-control input_pass", 'placeholder' : 'confirm password'}), label = "")

    def clean(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("confirmpassword")
        if password1!= password2:
            raise forms.ValidationError("Passwords do not match!")
        return self.cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username has already been taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("This email has already been registered!")
        return email