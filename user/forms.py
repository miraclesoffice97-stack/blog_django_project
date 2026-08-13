from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import views as authviews
from django.contrib import messages
from .models import Profile
from blog.models import Post
from django.shortcuts import redirect, reverse

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length= 100)
    last_name = forms.CharField(max_length= 100)
    email= forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
class PasswordResetComplete(authviews.PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Password Reset Successful')
        return redirect ('user-login')
        
class LoginForm(authviews.LoginView):
    template_name = 'user/login.html'
    def form_valid(self, form):
        messages.success(self.request, 'Login Successfully!')
        return super().form_valid(form)
        
    def get_success_url(self):
        if not self.request.user.profile.onboarded:
            return reverse('user-image_init')
        return reverse('blog-home')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'banner', 'profile_image']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']


class BannerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['banner']


class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
        def form_valid(self, form):
            form.instance.author = self.request.user
            super().form_valid(form)
        
        
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']