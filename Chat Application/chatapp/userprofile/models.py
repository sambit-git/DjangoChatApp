from django.db import models
from django.contrib.auth.models import User
from .util import resizeAndPad
from PIL import Image
import scipy.misc

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'userprofile/images/default.png', upload_to='userprofile/images/')
    lastActive = models.DateTimeField(null=True, blank=True, auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super(UserProfile,self).save(*args, **kwargs)
        print(self.image.path)
        img = Image.fromarray(resizeAndPad(self.image.path)).convert("L")
        img.save(self.image.path)