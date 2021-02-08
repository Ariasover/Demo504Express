"""Circles URLs."""

# Django
from django.urls import path

# Views
from .views.users import *

urlpatterns = [
    path('',LoginView.as_view(),name="login"),
    path('users/logout',LogoutView.as_view(),name="logout"),
    path('users/index',IndexView.as_view(),name="index"),
    path('users/list',UsersListView.as_view(),name="users_list"),
    path('users/create',UsersCreateView.as_view(),name="users_create"),
    path('messages/update/<int:pk>/',UsersUpdateView.as_view(),name="users_update"),

    # path('users/signup',UserSignupAPIView.as_view(),name="signup"),
    # path('users/verify',AccountVerificationAPIView.as_view(),name="verify"),
]