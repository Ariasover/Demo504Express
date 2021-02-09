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
    # path('users/update',UsersUpdateView.as_view(),name="users_update"),
    path('users/update/<int:pk>/',UsersUpdateView.as_view(),name="users_update"),

    # Groups
    path('groups/list',GroupView.as_view(),name="groups_list"),
    path('groups/create',GroupCreateView.as_view(),name="groups_create"),
    # path('groups/update/<int:pk>/',GroupUpdateView.as_view(),name="groups_update"),

]