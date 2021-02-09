"""Messages URLs."""

# Django
from django.urls import path

# Views
from .views.speech import *

urlpatterns = [

    path('speech/list',SpeechConfigurationView.as_view(),name="list"),
    path('speech/create',SpeechCreateView.as_view(),name="create"),
    path('speech/delete/<int:pk>/',SpeechDeleteView.as_view(),name="delete"),
    path('speech/update/<int:pk>/',SpeechUpdateView.as_view(),name="update"),
    
]