""" User's Views """

# Django 
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse




class ConfigurationView(View):
    def get(self, request):
	return render(request, 'index.html')
