from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import tp_DeviceData, cl_DeviceData, ss_DeviceData

# Register your models here.

@admin.register(tp_DeviceData)
@admin.register(cl_DeviceData)
@admin.register(ss_DeviceData)


class tp_DeviceData(ImportExportModelAdmin):
	pass

class cl_DeviceData(ImportExportModelAdmin):
	pass

class ss_DeviceData(ImportExportModelAdmin):
	pass




