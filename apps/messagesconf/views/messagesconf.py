""" User's Views """

# Django 
from django.contrib.auth import authenticate,logout,login
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.contrib import messages
from django.db import transaction


# Models
from apps.messagesconf.models.messagesconf import *


# Utils
from apps.utils.chrome_version import get_chrome_version


# Forms
from ..forms import MessagesConfigurationForm


# Openpyxl
from openpyxl import load_workbook


# Selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Local
import socket,os,plistlib,datetime
from pathlib import Path
from sys import platform
from time import sleep



class ConfigurationView(View):
	def get(self, request):
		return render(request, 'configuration.html')


class DashboardAereoView(ListView):
	template_name = 'dashboard_aereo.html'
	queryset = MessagesList.objects.all()
	paginate_by = 5
	no_of_message = 1
	no_enviado = MessageListStatus.objects.get(description__icontains='No Enviado')
	enviado = MessageListStatus.objects.get(description='Enviado')
	error = MessageListStatus.objects.get(description__icontains='Error')
	
	def verify_excel(self, departure_date):
		message_list = MessagesList.objects.filter(departure_date=departure_date)
		for instance in message_list:
			if not len(instance.phone) == 11:
				error_number = ErrorNumber()
				error_number.message_list = instance
				error_number.creation_user=self.request.user
				error_number.modification_user=self.request.user
				error_number.save()

				# Update message list with error
				message_list.filter(pk=instance.pk).update(status = self.error)

				

	# def get_chrome_driver(self):
	# 	if platform == "linux" or platform == "linux2" or platform == "darwin":
	# 		os.chmod(str(settings.BASE_DIR)+'/chromedriver', 755)
	# 		plistloc = "/Applications/Google Chrome.app/Contents/Info.plist"
	# 		pl = plistlib.readPlist(plistloc)
	# 		chrome_server_version = pl["CFBundleShortVersionString"]
	# 		chrome_server_version = chrome_server_version[0]+chrome_server_version[1] #for example '87' #TODO CAMBIAR ESTE METODO POR EL DE CHROMDRIVER()PARA OBTENER MEJOR LA VERSION
	# 		driver = webdriver.Chrome(executable_path=str(settings.VIRTUALENV_DIR)+'/lib/python3.7/site-packages/chromedriver_autoinstaller/'+chrome_server_version+'/chromedriver')
	# 	else:
	# 		chrome_server_version = get_chrome_version
	# ()
	# 		chrome_server_version = chrome_server_version[0]+chrome_server_version[1] #for example '87' #TODO CAMBIAR ESTE METODO POR EL DE CHROMDRIVER()PARA OBTENER MEJOR LA VERSION
	# 		driver = webdriver.Chrome(executable_path=str(settings.VIRTUALENV_DIR)+"\Lib\site-packages\chromedriver_autoinstaller\\"+chrome_server_version+"\chromedriver.exe")		
	# 	return driver


	def send_messages(self):
		customer_list = MessagesList.objects.filter(status=self.no_enviado).order_by('-pk')

		# Verificar que la lista de clientes excluya los clientes que estan en errores
		
		message_configuration = MessagesConfiguration.objects.get(is_active=True).text
		message_text=""
		xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
		invalid_xpath = '/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div'
		time=20

		if customer_list.exists():	 
			if platform == "linux" or platform == "linux2" or platform == "darwin":
				plistloc = "/Applications/Google Chrome.app/Contents/Info.plist"
				pl = plistlib.readPlist(plistloc)
				chrome_server_version = pl["CFBundleShortVersionString"]
				chrome_server_version = chrome_server_version[0]+chrome_server_version[1] #for example '87' #TODO CAMBIAR ESTE METODO POR EL DE CHROMDRIVER()PARA OBTENER MEJOR LA VERSION
				driver = webdriver.Chrome(executable_path=str(settings.VIRTUALENV_DIR)+'/lib/python3.7/site-packages/chromedriver_autoinstaller/'+chrome_server_version+'/chromedriver')
			else:
				chrome_server_version = get_chrome_version()
				chrome_server_version = chrome_server_version[0]+chrome_server_version[1] #for example '87' #TODO CAMBIAR ESTE METODO POR EL DE CHROMDRIVER()PARA OBTENER MEJOR LA VERSION
				driver = webdriver.Chrome(executable_path=str(settings.VIRTUALENV_DIR)+"\Lib\site-packages\chromedriver_autoinstaller\\"+chrome_server_version+"\chromedriver.exe")	
			
			driver.get("http://web.whatsapp.com")
			# sleep(5) # Cambiar si es necesario
			text_box=""
			for count,customer in enumerate(customer_list):
				print('CLIENTE',customer.name,' telefono: ', customer.phone)  
				try:
					print('MAMADO1')
					message_text = message_configuration.replace('/name/',customer.name)
					message_text = message_text.replace('/fecha/',str(customer.departure_date))
					message_text = message_text.replace('/monto/','{:0,.2f}'.format(customer.amount))
					message_text = message_text.replace('/pesomayor/',customer.weight_greather)
					message_text = message_text.replace('/tipo_peso/',customer.weight_type)
					driver.get(
						"https://web.whatsapp.com/send?phone={}&source=&data=#".format(str(customer.phone)))
					# TODO
					try:
						print('MAMADO2')
						driver.switch_to_alert().accept()
						print('MAMADO3')
					except Exception as e:
						print('Error',e)					
					sleep(5)

					print('MAMADO4')
					invalid_number_popup = driver.find_elements_by_xpath(invalid_xpath)
					print('encontro el popup',invalid_number_popup)
					if not invalid_number_popup:
						print('MAMADO5')
						WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
						text_box=driver.find_element(By.XPATH, xpath)
						print('MAMADO6')
						for part in message_text.split('\n'):
							text_box.send_keys(part)
							ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
						ActionChains(driver).send_keys(Keys.RETURN).perform()
						customer_list.filter(pk=customer.pk).update(status = self.enviado) #Todo
						print('Enviado',count+1)
					if count == 20 or count == 40 or count == 60 or count == 80 or count == 100 or count ==120:
						sleep(2)
					else:	
						error = ErrorNumber()
						error.message_list = customer
						error.creation_user=self.request.user
						error.modification_user=self.request.user
						error.save()

				except Exception as e:
					print('NOT SENT ===',e)

					# if not ErrorNumber.objects.filter(message_list=customer).exists():	
					# 	error = ErrorNumber()
					# 	error.message_list = customer
					# 	error.creation_user=self.request.user
					# 	error.modification_user=self.request.user
					# 	error.save()
				continue
			messages.success(self.request, 'Mensajes enviados',extra_tags='success')
			driver.quit()
		else:
			messages.error(self.request, 'No hay destinatarios',extra_tags='error')

	def post(self, request):
		if request.POST['options'] == "send_all":
			# Get a list of not sent messages
			self.send_messages()
		elif request.POST['options'] == 'upload_excel':
			try: 
				with transaction.atomic():
					file = request.FILES['myfile']
					if file.name.endswith('xlsx'): #Verify extension
						doc = load_workbook(file,data_only=True)
						nombres_hojas = doc.sheetnames
						hoja1 = doc.get_sheet_by_name(nombres_hojas[0])
						mayor = 0     
						x=4
						print('Numero mayor de la hoja',mayor)

						# Verificar el excel linea por linea.
						for y in range(4,1000):
							# print('y inicia en ',y)
							if not hoja1['B'+str(y)].value == None:
								mayor=mayor+1
							else:
								break
						departure_date = datetime.datetime.strptime(str(hoja1['J1'].value), '%Y-%m-%d %H:%M:%S')		
						departure_date = departure_date.date()

						for i in range (4, mayor+4):	
							if not hoja1['N'+str(i)].value == '#VALUE!' or not hoja1['N'+str(i)].value == '#N/A':
								if  not hoja1['C'+str(i)].value == None:
									messages_list = MessagesList()
									messages_list.name=hoja1['B'+str(i)].value
									messages_list.phone="504"+str(hoja1['C'+str(i)].value) 


									messages_list.departure_date = departure_date
									messages_list.amount = hoja1['P'+str(i)].value
									messages_list.weight_greather = hoja1['N'+str(i)].value
									messages_list.weight_type = hoja1['M'+str(i)].value
									messages_list.creation_user=self.request.user
									messages_list.modification_user=self.request.user
									messages_list.status = self.no_enviado
									messages_list.save()
									

									x = x + 1

						self.verify_excel(departure_date)
						messages.success(request, '¡Archivo subido y verificado con éxito!', extra_tags='success')
					else:
						messages.error(request, 'La extensión del archivo es incorrecta', extra_tags='error')
			except Exception as e:
				print('error',e)
				messages.error(request, 'No se ha podido subir el archivo', extra_tags='error')

		return HttpResponseRedirect('/messages/dashboard-aereo')
	

	def get_context_data(self, **kwargs):
		no_enviados = MessageListStatus.objects.get(description__icontains='No Enviado')
		context = super().get_context_data(**kwargs)
		not_sent_messages= self.queryset.filter(status=no_enviados)[:5]
		quantity_not_sent= len(self.queryset.filter(status=no_enviados))

		sent_messages= self.queryset.filter(status=1)
		quantity_sent= len(sent_messages)

		context.update({
			'sent_messages': sent_messages[:5],
			'not_sent_messages': not_sent_messages,
			'quantity_not_sent':quantity_not_sent,
		 	'quantity_sent':quantity_sent
		})		
		return context





class SpeechConfigurationView(ListView):
	template_name = 'speech_configuration.html'
	queryset = MessagesConfiguration.objects.filter()
	paginate_by = 5

	def post(self,request):
		print('hice post')
		if request.POST['options'] == "activate":
			# SEND MESSAGES
			# DESACTIVAR LAS QUE ESTAN ACTIVAS
			MessagesConfiguration.objects.all().update(is_active=False)
			messages_configuration = MessagesConfiguration.objects.get(pk=request.POST['pk'])
			messages_configuration.is_active = True
			messages_configuration.save()

		elif request.POST['options'] == "deactivate":
			messages_configuration = MessagesConfiguration.objects.get(pk=request.POST['pk'])
			messages_configuration.is_active = False
			messages_configuration.save()

		return HttpResponseRedirect('/messages/speech-configuration')		


class SpeechCreateView(CreateView):
	model = MessagesConfiguration
	template_name = 'create_speech_configuration.html'
	form_class = MessagesConfigurationForm
	
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.creation_user = self.request.user
		self.object.modification_user = self.request.user
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())
	
	def get_success_url(self):
		return reverse('messagesconf:speech_configuration')


class SpeechUpdateView(UpdateView):
	model = MessagesConfiguration
	template_name = 'create_speech_configuration.html'
	form_class = MessagesConfigurationForm

	def get_success_url(self):
		return reverse('messagesconf:speech_configuration')

	
class SpeechDeleteView(DeleteView):
	model = MessagesConfiguration 
	template_name = 'confirm_delete.html'

	def get_success_url(self):
		return reverse('messagesconf:speech_configuration')