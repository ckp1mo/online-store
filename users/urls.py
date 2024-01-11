from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, generate_new_password, VerificationView, \
    error_verification

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', VerificationView.as_view(), name='verification'),
    path('verification/verify_error/', error_verification, name='verify_email_error'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/generate_new_password', generate_new_password, name='generate_new_password'),
]
