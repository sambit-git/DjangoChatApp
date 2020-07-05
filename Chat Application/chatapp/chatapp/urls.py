from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, register_view, logout_view
from chat import urls
from userprofile import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('logout/', logout_view, name='logout'),
    path('chat/', include('chat.urls', namespace='chat')),
    path('profile/', include('userprofile.urls', namespace='profile')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)