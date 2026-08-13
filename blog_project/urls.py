from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from user.views import SignUp as SignupView
from user.forms import LoginForm, PasswordResetComplete
from user.views import ProfilePage as user_profile, ProfileEditPage, image_init, banner_init, bio_init
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.url')),
    path('login/', LoginForm.as_view(), name= "user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'user/logout.html'), name = "user-logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'user/reset_password.html'), name = "password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name= 'user/resetdone_password.html'), name = "password_reset_done"),
    path('password_reset_confirmation/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'user/resetconfirm_password.html'), name = "password_reset_confirm"),
    path('reset_successfull/', PasswordResetComplete.as_view(), name = "password_reset_complete"),
    path('signup/', SignupView, name = "user-signup"),
    path('profile/', user_profile, name='user-profile'),
    path('profile-uodate/', ProfileEditPage, name = 'user-profile_update'),
    path('profile_init_img/', image_init, name = 'user-image_init'),
    path('banner/', banner_init, name = 'user-banner'),
    path('bio/', bio_init, name = 'user-bio')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)