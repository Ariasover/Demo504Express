"""Messages URLs."""

# Django
from django.urls import path

# Views
from .views.messagesconf import ConfigurationView,DashboardView

urlpatterns = [
    path('messages/configuration',ConfigurationView.as_view(),name="configuration"),
    path('messages/dashboard',DashboardView.as_view(),name="dashboard"),
]