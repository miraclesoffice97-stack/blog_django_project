from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to = 'profile_image/')
    bio = models.CharField(max_length = 150, blank = True)
    banner = models.ImageField(default = 'default_banner.jpg', upload_to = 'profile_image/')
    onboarded = models.BooleanField(default = False)
