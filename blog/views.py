from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def post(request):
    post = Post.objects.all()
    context = {
    'posts': post
    }
    return render(request, "blog/home.html", context)

def About(request):
    data={
        'about': 'get latest tech news and insight on moknow.. the mono news agent'
    }
    return render(request, "blog/about.html", data)