from django.contrib import admin
from .models import MessagesList
from import_export.admin import ImportExportModelAdmin

@admin.register(MessagesList)
class usrdet(ImportExportModelAdmin):
    list_display = ('name','phone')

