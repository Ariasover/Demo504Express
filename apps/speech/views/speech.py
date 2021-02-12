""" User's Views """

# Django 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,UpdateView,CreateView,DeleteView
from django.contrib import messages


# Models
from ..models.speech import *
from ...messagesconf.models.messagesconf import *


# Forms
from ..forms import *


# Openpyxl
from openpyxl import load_workbook


# Filters
from ..filters import OrderFilter


class SpeechConfigurationView(ListView):
	model = MessagesConfiguration
	template_name = 'speech_configuration_list.html'
	paginate_by = 5


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["filter"] = OrderFilter(self.request.GET,queryset=self.get_queryset())
		return context
	
	def get_queryset(self):
		qs = self.model.objects.all()
		product_filtered_list = OrderFilter(self.request.GET, queryset=qs)
		return product_filtered_list.qs
	
	
	def post(self,request):
		if request.POST['options'] == "activate":
			MessagesConfiguration.objects.all().update(is_active=False)
			messages_configuration = MessagesConfiguration.objects.get(pk=request.POST['pk'])
			messages_configuration.is_active = True
			messages_configuration.save()

		elif request.POST['options'] == "deactivate":
			messages_configuration = MessagesConfiguration.objects.get(pk=request.POST['pk'])
			messages_configuration.is_active = False
			messages_configuration.save()

		return HttpResponseRedirect(reverse('speech:list'))		


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
		return reverse('speech:list')


class SpeechUpdateView(UpdateView):
	model = MessagesConfiguration
	template_name = 'create_speech_configuration.html'
	form_class = MessagesConfigurationForm

	def get_success_url(self):
		return reverse('speech:list')

	
class SpeechDeleteView(DeleteView):
	model = MessagesConfiguration 
	template_name = 'confirm_delete.html'

	def get_success_url(self):
		return reverse('speech:list')