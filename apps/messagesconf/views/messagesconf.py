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
from apps.messagesconf.models import *

# Forms
from ..forms import MessagesConfigurationForm

# Openpyxl
from openpyxl import load_workbook

# Time
from time import sleep

# Selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

# Local
import socket,os


class ConfigurationView(View):
	def get(self, request):
		return render(request, 'configuration.html')


class DashboardAereoView(ListView):
	template_name = 'dashboard_aereo.html'
	queryset = MessagesList.objects.all()
	paginate_by = 5
	no_of_message = 1

	def send_messages(self):
			
		message_text = MessagesConfiguration.objects.get(is_active=True).text
		customer_list = MessagesList.objects.filter(status=0)
		driver = webdriver.Chrome(executable_path="/Users/ariasover/Documents/chromedriver")
		driver.get("http://web.whatsapp.com")
		sleep(10)
		mensajes = 0
		
		for count,customer in enumerate(customer_list):
			message_text = message_text.replace('/name/',customer.name)
			message_text = message_text.replace('/fecha/',customer.departure_date)
			message_text = message_text.replace('/monto/','{:0,.2f}'.format(customer.amount))
			message_text = message_text.replace('/pesomayor/',customer.weight_greather)
			message_text = message_text.replace('/tipo_peso/',customer.weight_type)
			try:
				driver.get(
					"https://web.whatsapp.com/send?phone={}&source=&data=#".format(customer.phone))
				try:
					driver.switch_to_alert().accept()
				except Exception as e:
					pass
				xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
				time=30
				WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
				txt_box = driver.find_element(
				By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
				global no_of_message
				for x in range(self.no_of_message):
					txt_box.send_keys(message_text)
					txt_box.send_keys("\n")

				
				customer_list.filter(pk=customer.pk).update(status = 1)
				print('MENSAJE',count+1)
				print('Estado Actualizado')
				mensajes = count+1

				
			except Exception as e:
				print('SEND WHA===',e)
			break #TODO ESTE BREAK SIRVE PARA PODER ENVIAR SOLAMENTE UN MENSAJE
		print('CERRANDO CHROME') #TODO
		messages.success(self.request, 'Se enviaron '+str(mensajes)+ ' mensajes')
		driver.quit()	

	def post(self, request):
		if request.POST['options'] == "send_all":
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
							print('y inicia en ',y)
							if not hoja1['A'+str(y)].value == None:
								mayor=mayor+1
							else:
								break
						print('verificar el numero mayor',mayor)
						for i in range (4, mayor+4):
							print('VERIFICAR C',hoja1['C'+str(i)].value)
							print('VERIFICAR EL LEN',len([hoja1['C'+str(i)].value]))
							if not hoja1['N'+str(i)].value == '#VALUE!' or not hoja1['N'+str(i)].value == '#N/A':
								if  not hoja1['C'+str(i)].value == None:
									messages_list = MessagesList()
									messages_list.name=hoja1['B'+str(i)].value
									messages_list.phone=hoja1['C'+str(i)].value #TODO SUSTITUIR ESTO POR hoja1['LETRA'+str(i)].value
									# messages_list.phone='50496068888' #TODO SUSTITUIR ESTO POR hoja1['LETRA'+str(i)].value
									messages_list.departure_date = hoja1['M2'].value
									messages_list.amount = hoja1['N'+str(i)].value
									messages_list.weight_greather = hoja1['M'+str(i)].value
									messages_list.weight_type = hoja1['L'+str(i)].value
									messages_list.creation_user=self.request.user
									messages_list.modification_user=self.request.user
									messages_list.save()
									x = x + 1
								messages.success(request, '¡Archivo subido con éxito!', extra_tags='success')
					else:
						messages.error(request, 'La extensión del archivo es incorrecta', extra_tags='error')
			except Exception as e:
				print('error',e)
				messages.error(request, 'No se ha podido subir el archivo', extra_tags='error')

		return HttpResponseRedirect('/messages/dashboard-aereo')
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		not_sent_messages= self.queryset.filter(status=0)[:5]
		quantity_not_sent= len(self.queryset.filter(status=0))

		sent_messages= self.queryset.filter(status=1)
		quantity_sent= len(sent_messages)

		context.update({
			'sent_messages': sent_messages[:5],
			'not_sent_messages': not_sent_messages,
			'quantity_not_sent':quantity_not_sent,
		 	'quantity_sent':quantity_sent
		})		
		return context


# class DashboardMaritimoView(ListView):
# 	template_name = 'dashboard_maritimo.html'
# 	queryset = MessagesList.objects.all()
# 	paginate_by = 5
# 	no_of_message = 1
# 	def initalize(self):
			
# 		# message_text = '*Prueba 3, automatizacion de Whatsapp por medio de Python*'
# 		message_text = MessagesConfiguration.objects.get(is_active=True).text
# 		# no_of_message = 1  # no. de tiempo desea que el mensaje sea enviado
# 		# lista de números de teléfono puede ser de cualquier longitud
# 		# Puedes agregar a la lista mas de un numero ejem  [573024508559,num2,num3,num4]

# 		messages_list = MessagesList.objects.filter(status=0)
# 		driver = webdriver.Chrome(executable_path="/Users/ariasover/Documents/chromedriver")
# 		driver.get("http://web.whatsapp.com")
# 		sleep(10)

		

# 		for count,moblie_no in enumerate(messages_list):
# 			# REPLACE TEXT IN MESSAGE
# 			print('VERIFICAR NOMBRE',moblie_no.name)
			
			
# 			message_text = message_text.replace('/name/',moblie_no.name)
# 			message_text = message_text.replace('/fecha/',moblie_no.departure_date)
# 			message_text = message_text.replace('/monto/','{:0,.2f}'.format(moblie_no.amount))
# 			message_text = message_text.replace('/pesomayor/',moblie_no.weight_greather)
# 			message_text = message_text.replace('/tipo_peso/',moblie_no.weight_type)
# 			print('TEXTO REEMPLAZADO',message_text)

# 			# ================HEAVY PROCESS==================
# 			try:
# 				driver.get(
# 					"https://web.whatsapp.com/send?phone={}&source=&data=#".format(moblie_no.phone))
# 				try:
# 					driver.switch_to_alert().accept()
# 				except Exception as e:
# 					pass
# 				# print('')
# 				xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
# 				time=30
# 				WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
				
# 				txt_box = driver.find_element(
# 				By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
# 				global no_of_message
# 				for x in range(self.no_of_message):
# 					txt_box.send_keys(message_text)
# 					txt_box.send_keys("\n")

				
# 				messages_list.filter(pk=moblie_no.pk).update(status = 1)
# 				print('MENSAJE',count+1)
# 				print('Estado Actualizado')

				
# 			except Exception as e:
# 				print('SEND WHA===',e)
# 			break
# 		print('CERRANDO CHROME')
# 		driver.quit()	

# 	def post(self, request):
# 		if request.POST['options'] == "send_all":
# 			# SEND MESSAGES
# 			self.initalize()
# 		elif request.POST['options'] == 'excel':
# 			exito = ''
# 			error = ''
# 			try: 
# 				file = request.FILES['myfile']
# 				from openpyxl import load_workbook
# 				try:
# 					# GET FILE INFORMATION
# 					doc = load_workbook(file,data_only=True)
# 					nombres_hojas = doc.sheetnames
# 					hoja1 = doc.get_sheet_by_name(nombres_hojas[0])
# 					hoja2 = doc.get_sheet_by_name(nombres_hojas[1])
# 					mayor1 = hoja1.max_row      
# 					# mayor2 = hoja2.max_row      
# 					x=4
# 					# print('VERIFICAR QUE PUEDO LEER LA HOJA',hoja1['B4'].value)
# 					print('Importando...')
# 					for i in range (4, 171):
# 						# CREATE AN INSTANCE OF MODEL
						
# 						# print('Nombre',hoja1['B'+str(i)].value)
# 						messages_list = MessagesList()
# 						messages_list.name=hoja1['B'+str(i)].value
# 						messages_list.phone='50496068888' #TODO SUSTITUIR ESTO POR hoja1['LETRA'+str(i)].value

# 						messages_list.departure_date = hoja1['L2'].value
# 						messages_list.amount = hoja1['N'+str(i)].value
# 						messages_list.weight_greather = hoja1['M'+str(i)].value
# 						messages_list.weight_type = hoja1['L'+str(i)].value

# 						messages_list.creation_user=self.request.user
# 						messages_list.modification_user=self.request.user
# 						messages_list.save()
# 						x = x + 1
#                     messages.success('Informacion cargada con exito')
# 					exito = 'Información cargada con éxito'
# 				except Exception as e:
# 					print('error',e)
# 					error = 'Surgio un error al cargar información'
				
# 				exito = 'Información cargada con éxito'

# 			except Exception as e:
# 				print('error', e)
# 				#raise e
# 				error = 'Surgio un error al cargar información'

	

# 			# person_resource = MessagesListResource()
# 			# dataset = Dataset()
# 			# new_persons = request.FILES['myfile']
# 			# try:
# 			# 	imported_data = dataset.load(new_persons.read(), format='xlsx')
# 			# 	result = person_resource.import_data(dataset, dry_run=True,raise_errors=True)
# 			# except Exception as e:
# 			# 	print('ERRORES',e)
# 		else:
# 			print('hice post')
				
# 		return HttpResponseRedirect('/messages/dashboard-maritimo')
	

# 	def get_context_data(self, **kwargs):
# 		# Call the base implementation first to get a context
# 		context = super().get_context_data(**kwargs)
# 		not_sent_messages= self.queryset.filter(status=0)[:5]
# 		quantity_not_sent= len(self.queryset.filter(status=0))

# 		sent_messages= self.queryset.filter(status=1)
# 		quantity_sent= len(sent_messages)

# 		context.update({
# 			'sent_messages': sent_messages[:5],
# 			'not_sent_messages': not_sent_messages,
# 			'quantity_not_sent':quantity_not_sent,
# 		 	'quantity_sent':quantity_sent
# 		})		
# 		return context


class SpeechConfigurationView(ListView):
	template_name = 'speech_configuration.html'
	queryset = MessagesConfiguration.objects.filter()
	paginate_by = 5
	no_of_message = 1
	
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