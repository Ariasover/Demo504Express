"""Messages URLs."""

# Django
from django.urls import path

# Views
from .views.messages import ConfigurationView

urlpatterns = [
    path('messages/configuration',ConfigurationView.as_view(),name="configuration"),
]