from django.shortcuts import render
from .forms import UpdateProfile
from .models import UserProfile
# Create your views here.

def update_profile(request):
    if request.method == "POST":
        form = UpdateProfile(request.POST, request.FILES,instance=request.user.userprofile)
        form.save()
    else:
        form = UpdateProfile()
    context = {
        'form' : form
    }

    return render(request, "userprofile/updateprofile.html", context)