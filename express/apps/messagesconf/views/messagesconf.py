""" User's Views """

# Django 
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from apps.messagesconf.models import *
from django.views.generic import ListView
from tablib import Dataset
from apps.messagesconf.resources import MessagesListResource
from apps.messagesconf.models import MessagesList, MessagesConfiguration


# Messages Configuration
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket,os


  # esperar tiempo para escanear el código en segundo
	# return True



class ConfigurationView(View):
	def get(self, request):
		return render(request, 'configuration.html')

class DashboardView(ListView):
	template_name = 'dashboard.html'
	queryset = MessagesList.objects.all()
	paginate_by = 5
	no_of_message = 1
	def initalize(self):
			
		message_text = '*Prueba 3, automatizacion de Whatsapp por medio de Python*'
		message_text = MessagesConfiguration.objects.last().text
		# no_of_message = 1  # no. de tiempo desea que el mensaje sea enviado
		# lista de números de teléfono puede ser de cualquier longitud
		# Puedes agregar a la lista mas de un numero ejem  [573024508559,num2,num3,num4]

		moblie_no_list = MessagesList.objects.all()
		driver = webdriver.Chrome(executable_path="/Users/ariasover/Documents/chromedriver")
		driver.get("http://web.whatsapp.com")
		sleep(10)


		for count,moblie_no in enumerate(moblie_no_list):
			# ================HEAVY PROCESS==================
			try:
				driver.get(
					"https://web.whatsapp.com/send?phone={}&source=&data=#".format(moblie_no.phone))
				try:
					driver.switch_to_alert().accept()
				except Exception as e:
					pass
				# print('')
				xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
				time=30
				WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
				
				txt_box = driver.find_element(
				By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
				global no_of_message
				for x in range(self.no_of_message):
					txt_box.send_keys(message_text)
					txt_box.send_keys("\n")

				# aqui se termina de enviar el mensaje
				print('MENSAJE',count)

			except Exception as e:
				print('SEND WHA===',e)
			

	def post(self, request):
		# print('request',request.POST)
		if request.POST['options'] == "send_all":
			# SEND MESSAGES
			self.initalize()
		elif request.POST['options'] == 'excel':
			print('elegi excel')
		else:
			person_resource = MessagesListResource()
			dataset = Dataset()
			new_persons = request.FILES['myfile']
			try:
				imported_data = dataset.load(new_persons.read(), format='xlsx')
				result = person_resource.import_data(dataset, dry_run=True,raise_errors=True)
			except Exception as e:
				print('ERRORES',e)
				
		return HttpResponseRedirect('/messages/dashboard')
	

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		not_sent_messages= self.queryset.filter(status=0)[:10]
		quantity_not_sent= len(not_sent_messages)

		sent_messages= self.queryset.filter(status=1)
		quantity_sent= len(sent_messages)

		context.update({
			'sent_messages': sent_messages[:5],
			'not_sent_messages': not_sent_messages,
			'quantity_not_sent':quantity_not_sent,
		 	'quantity_sent':quantity_sent
		})		
		return context



	