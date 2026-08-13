from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length = 100, null = False)
    content = models.TextField(null=False)
    
    date = models.DateTimeField(auto_now_add = True)
    
    image = models.ImageField(upload_to = "content_image/", blank = True)
