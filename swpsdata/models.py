from django.db import models

# Create your models here.

class DeviceData(models.Model):
	name 		= models.CharField(max_length=50, blank=True)
	gender 		= models.CharField(max_length=10, blank=True)
	adhaarNo 	= models.CharField(max_length=20, blank=True)
	contactNo 	= models.CharField(max_length=10, blank=True)
	address 	= models.CharField(max_length=200, blank=True)
	village 	= models.CharField(max_length=30, blank=True)
	mandal 		= models.CharField(max_length=30, blank=True)
	district 	= models.CharField(max_length=30, blank=True)
	pincode 	= models.CharField(max_length=10, blank=True)
	poNo 		= models.CharField(max_length=30, blank=True)
	longitude 	= models.CharField(max_length=10, blank=True)
	latitude 	= models.CharField(max_length=10, blank=True)
	devNo 		= models.CharField(max_length=20, blank=True)
	conMake 	= models.CharField(max_length=30, blank=True)
	dateInst 	= models.DateField()
	InstName 	= models.CharField(max_length=50, blank=True)
	pumpMfg 	= models.CharField(max_length=30, blank=True)
	pvMake	 	= models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.devNo+'-'+self.InstName+'-'+self.conMake+'-'+self.pumpMfg
