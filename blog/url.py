from django.urls import path
from .views import post as BlogPostView
from .views import About
from user.views import PostView, PostUpdateView, DeletePostView, SinglePostView, PostlinkView, SpecificProfileView

urlpatterns = [
    path('', BlogPostView, name='blog-home'),
    path('about/', About, name='blog-about'),
    path('post/', PostView, name='blog-post'),
    path('update_post/<int:pk>/', PostUpdateView, name='blog-post_update'),
    path('delete_post/<int:pk>/', DeletePostView, name='blog-post_delete'),
    path('post/<int:pk>/', SinglePostView, name='blog-apost'),
    path('sharepost/<int:pk>/', PostlinkView, name='share-post'),
    path('profile/<str:username>/', SpecificProfileView, name = 'user-specific_profile'),
]
