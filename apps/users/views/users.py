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

# Forms
from ..forms import *


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
	queryset = User.objects.filter()
	context_object_name = 'users_list'
	paginate_by = 5

	# def get(self):
    # 	return render(request, 'users.html')

	def post(self,request):
		if request.POST['options'] == "activate":
			user = User.objects.get(pk=request.POST['pk'])
			user.is_active = True
			user.save()

		elif request.POST['options'] == "deactivate":
			user = User.objects.get(pk=request.POST['pk'])
			user.is_active = False
			user.save()

		return HttpResponseRedirect(reverse('users:users_list'))



class UsersCreateView(CreateView):
	model = User
	template_name = 'users-create.html'
	form_class = CustomUserCreationForm
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()
		return HttpResponseRedirect(reverse('users:users_list'))