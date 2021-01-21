""" User's Views """

# Django 
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

# Model
from apps.messagesconf.models.messagesconf import ChromeDriverVerification

# Local
import requests, zipfile, io, socket,os
from sys import platform





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
			response = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
			version = ChromeDriverVerification.objects.filter(version=str(response.text)).last()
			print('VERIFICAR VERSION DE CHROME EN BD',version)
			print('VERIFICAR VERSION DE CHROME EN google',str(response.text))
			
			if not  str(version) == str(response.text):
				print('son diferentes')
				if platform == "linux":
					r = requests.get('https://chromedriver.storage.googleapis.com/'+response.text+'/chromedriver_linux64.zip')
				elif platform == "darwin":
					r = requests.get('https://chromedriver.storage.googleapis.com/'+response.text+'/chromedriver_mac64.zip')
				else:
					r = requests.get('https://chromedriver.storage.googleapis.com/'+response.text+'/chromedriver_win32.zip')
				
				ChromeDriverVerification.objects.create(version=str(response.text))
			
				z = zipfile.ZipFile(io.BytesIO(r.content))
				z.extractall(settings.BASE_DIR)
			
		except Exception as e:
			print('ERROR',e)
		
		return render(request, 'index.html')