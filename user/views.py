from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, BioForm, BannerForm, ImageForm, PostForm,PostUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import Post
from .models import Profile


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, f'Account created successfully {username}, Login!')
            return redirect('user-login')
            
    else:
        form = SignUpForm()
        
    context = {'form': form}
    return render(request, 'user/sign_up.html', context)
    

@login_required
def ProfilePage(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    user = request.user
    posts = Post.objects.filter(author= user)
    
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'user/profile.html', context)
    
    
@login_required
def ProfileEditPage(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, 'Update Successful!')
            return redirect('user-profile')
            
    else:  
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'user/profile_update.html', context)


@login_required
def image_init(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    user = request.user
    if request.method == "POST":
        i_form = ImageForm(request.POST, request.FILES, instance = request.user.profile)
        
        if i_form.is_valid():
            user.profile.onborded = True
            user.profile.save()
            i_form.save()
            return redirect('user-banner')
        
    else:
        i_form = ImageForm(request.FILES, instance = user.profile)
        user.profile.onboarded = True
        user.profile.save()
        
    context = {
        'user': user,
        'i_form': i_form
    }
    return render(request, 'user/profile_init.html', context)
    
    
@login_required
def banner_init(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    user = request.user
    if request.method == "POST":
        b_form = BannerForm(request.POST, request.FILES, instance = request.user.profile)
        
        if b_form.is_valid():
            b_form.save()
            return redirect('user-bio')
        
    else:
        b_form = ImageForm(request.FILES, instance = user.profile)
        
    context = {
        'user': user,
        'b_form': b_form
    }
    return render(request, 'user/banner_init.html', context)
    
    
@login_required
def bio_init(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    user = request.user
    if request.method == "POST":
        bio_form = BioForm(request.POST, instance = user.profile)
        
        if bio_form.is_valid():
            bio_form.save()
            return redirect('blog-home')
        
    else:
        bio_form = BioForm(instance = user.profile)
        
    context = {
        'user': user,
        'bio_form': bio_form
    }
    return render(request, 'user/bio_init.html', context)
    
    
@login_required
def PostView(request):
    post = Post
    if request.method == "POST":
        ps_form = PostForm(request.POST, request.FILES)
        
        if ps_form.is_valid():
            post = ps_form.save(commit = False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post upload successful!')
            return redirect('blog-home')
    else:
        ps_form = PostForm()
            
    context = {
        'ps_form': ps_form,
        'post': post
    }
    return render(request, 'blog/post.html', context)
    
    
def PostUpdateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:
        messages.error(request, 'denied can not update someone elses post!')
        return redirect('blog-home')
        
    else:
        if request.method == "POST":
            psu_form = PostUpdateForm(request.POST, request.FILES, instance= post)
            
            if psu_form.is_valid():
                psu_form.save()
                messages.success(request, 'Post update')
                return redirect('blog-home')
                
        else:
            psu_form = PostUpdateForm(instance= post)
            
        context = {
            'psu_form': psu_form,
            'post': post
        }
        return render(request, 'blog/post_update.html', context)
        
        
@login_required
def DeletePostView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:
        messages.error(request, 'denied can not delete someone elses post!')
        return redirect('blog-home')
        
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('blog-home')
        
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete.html', context)
    
@login_required
def SinglePostView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context ={
        'post': post
    }
    return render(request, 'blog/apost.html', context)
    
    
def PostlinkView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    link = request.build_absolute_uri(reverse('blog-apost', args=[pk]))
    context ={
        'link': link
    }
    return render(request, context)
    

def SpecificProfileView(request, username):
    user_profile = get_object_or_404(User, username= username)
    posts = user_profile.post_set.all()
    
    context = {
        "user_profile": user_profile,
        'posts': posts
    }
    
    return render(request, 'blog/profile.html', context)
    