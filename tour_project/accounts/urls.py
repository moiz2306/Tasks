from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, UserLoginView, UserLogoutView, UserUpdateView, UserDeleteView, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('update_profile/', UserUpdateView.as_view(), name='update_profile'),
    path('delete_profile/', UserDeleteView.as_view(), name='delete_profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
