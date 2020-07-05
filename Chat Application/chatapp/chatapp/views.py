from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from userprofile.models import UserProfile
from datetime import datetime
from django.db.models.signals import post_save
from userprofile.models import UserProfile

def home_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    print("Authenticated User: ",request.user.is_authenticated)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            # print("User is not registered")
            msg = 'Username or password is incorrect.'
        else:
            # print("Attempting to log in : ",user)
            login(request, user)
            user.userprofile.status = True
            user.userprofile.save()
            return redirect('chat:home')
    context = {
        "form" : form,
        "title" : "Home Page",
        "form_name" : "login",
        'msg' : msg
    }
    return render(request, 'base/home.html', context)

def register_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = User.objects.create_user(username = username, email = email, password = password)
        # Log the user in and navigate to profile update page
        user = authenticate(request, username=username, password=password)
        login(request, user)
        user.userprofile.status = True
        user.userprofile.save()
        return redirect('profile:update')
        return redirect('chat:home')
    context = {
        "form" : form,
        "title" : "Registration Page",
        "form_name" : "register"
    }
    return render(request, 'base/home.html', context)

def logout_view(request):
    user = User.objects.get(username = request.user.username)
    user.userprofile.status = False
    user.userprofile.lastActive = datetime.now()
    user.userprofile.save()
    logout(request)
    return redirect('home')

def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        print("-"*80)
        profile = UserProfile.objects.create(user = instance)


post_save.connect(create_profile, sender=User)