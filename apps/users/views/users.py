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
			print('verificar')
			chromedriver_autoinstaller.install()
			print('verificar2',chromedriver_autoinstaller)
			
				
				# plistloc = "/Applications/Google Chrome.app/Contents/Info.plist"
				# pl = plistlib.readPlist(plistloc)
				# chrome_server_version = pl["CFBundleShortVersionString"]
				# chrome_server_version = chrome_server_version[0]+chrome_server_version[1] #for example '87'	
				# print('aqui1')			
				# chrome_online_version = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE_'+chrome_server_version) #Example 87.43.44.4
				# print('aqui2')
				# chrome_database_version = ChromeDriverVerification.objects.filter(version=str(chrome_server_version)).last()
				# print('aqui3')
				# if not str(chrome_server_version) == str(chrome_database_version):
					
				# 	r = requests.get('https://chromedriver.storage.googleapis.com/'+chrome_online_version.text+'/chromedriver_mac64.zip')
				# 	print('no puedo concatener')

			# ChromeDriverVerification.objects.create(version=str(chrome_server_version))
			# z = zipfile.ZipFile(io.BytesIO(r.content))
			# z.extractall(settings.BASE_DIR)


			# print(str(settings.BASE_DIR)+'/chromedriver')
			# /Users/ariasover/Documents/Proyectos/504ExpressEnv/
			# # Verificar la version de chrome actual
			# # chrome_path = 'C:\Program Files\Google\Chrome\Application'
			# plistloc = "/Applications/Google Chrome.app/Contents/Info.plist"
			# las_version_on_db = ChromeDriverVerification.objects.filter(version=str(online_version.text)).last()
			# # if not str(las_version_on_db) == str(online_version.text):
			# print('son diferentes')
			# 	# if platform == "linux":
			# 		# r÷ = requests.get('https://chromedriver.storage.googleapis.com/'+response.text+'/chromedriver_linux64.zip')
			# 	# elif platform == "darwin":
			# r = requests.get('https://chromedriver.storage.googleapis.com/'+'87.0.4280.88'+'/chromedriver_mac64.zip')
			# 	# else:
			# 		# r = requests.get('https://chromedriver.storage.googleapis.com/'+response.text+'/chromedriver_win32.zip')
				
			# 	# ChromeDriverVerification.objects.create(version=str(response.text))

			# z = zipfile.ZipFile(io.BytesIO(r.content))
			# z.extractall(settings.BASE_DIR)
			
		except Exception as e:
			print('ERROR',e)
		
		return render(request, 'index.html')