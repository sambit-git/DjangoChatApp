from django.urls import path
from .views import update_profile

app_name = 'userprofile'

urlpatterns = [
    path('', update_profile, name="update")
]