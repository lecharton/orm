# from django.contrib.auth.views import views as v
# import views from django.contrib.auth.views
import django.contrib.auth.views as v
from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),

    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('password_change/', v.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', v.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', v.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', v.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', v.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]