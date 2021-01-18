"""Circles URLs."""

# Django
from django.urls import path

# Views
from .views.users import LoginView,LogoutView,IndexView

urlpatterns = [
    path('',LoginView.as_view(),name="login"),
    path('users/logout',LogoutView.as_view(),name="logout"),
    path('users/index',IndexView.as_view(),name="index"),
    # path('users/signup',UserSignupAPIView.as_view(),name="signup"),
    # path('users/verify',AccountVerificationAPIView.as_view(),name="verify"),
]