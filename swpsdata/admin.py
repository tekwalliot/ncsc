from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DeviceData

# Register your models here.

@admin.register(DeviceData)


class DeviceData(ImportExportModelAdmin):
	pass




