"""Messages URLs."""

# Django
from django.urls import path

# Views
from .views.messagesconf import *

urlpatterns = [

    # Messages
    path('messages/dashboard-aereo',DashboardAereoView.as_view(),name="dashboard_aereo"),
    path('messages/one_message',OneMessageView.as_view(),name="one_message"),

]