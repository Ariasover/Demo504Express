""" User's Views """

# Django 
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View,ListView,UpdateView,CreateView,DeleteView,DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User


# Model
from apps.messagesconf.models.messagesconf import ChromeDriverVerification


# Local
import requests, zipfile, io, socket,os, plistlib

# Selenium
from selenium import webdriver

# ChromeDriver
import chromedriver_autoinstaller


class LoginView(View):
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

			else:
				return HttpResponse("Inactive user.")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)

		return render(request, "index.html")
	def get(self, request, **kwargs):     
		print(request)
		return render(request, 'login.html')


class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(settings.LOGIN_URL)


class IndexView(View):
	def get(self, request):
		# Comprobar speech activo.
		
		try:
			chromedriver_autoinstaller.install()
		except Exception as e:
			print('ERROR',e)
		
		return render(request, 'index.html')


class UsersListView(ListView):
    	
	model = User
	template_name = 'users-list.html'
	queryset = User.objects.filter(is_active=True)
	context_object_name = 'users_list'
	paginate_by = 4