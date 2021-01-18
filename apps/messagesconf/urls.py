"""Messages URLs."""

# Django
from django.urls import path

# Views
from .views.messagesconf import *

urlpatterns = [
    path('messages/configuration',ConfigurationView.as_view(),name="configuration"),
    path('messages/dashboard-aereo',DashboardAereoView.as_view(),name="dashboard_aereo"),
    # path('messages/dashboard-maritimo',DashboardMaritimoView.as_view(),name="dashboard_maritimo"),
    path('messages/speech-configuration',SpeechConfigurationView.as_view(),name="speech_configuration"),
    
    path('messages/create-speech-configuration',SpeechCreateView.as_view(),name="create_speech_configuration"),
    path('messages/delete-speech-configuration/<int:pk>/',SpeechDeleteView.as_view(),name="delete_speech_configuration"),
    path('messages/update-speech-configuration/<int:pk>/',SpeechUpdateView.as_view(),name="update_speech_configuration"),
    # path('messages/edit-speech/<int:pk>/update/',SpeechUpdateView.as_view(),name="edit_speech"),

]