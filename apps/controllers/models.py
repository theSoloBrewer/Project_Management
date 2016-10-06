from django.db import models
from apps.common import NetworkInfo
from apps.hardware.models import *
from apps.doors.models import *
from apps.projects.models import *

# Create your models here.
class Controller(models.Model):
	project = models.ForeignKey(Project)
	number = models.CharField(max_length=200)
	description = models.CharField(max_length=200, null=True, blank=True)
	serial = models.CharField(max_length=200, blank=True)
	#ports = models.ForeignKey(Port, blank=True)
	network = models.OneToOneField(NetworkInfo, null=True, blank=True, on_delete=models.SET_NULL)
	
	class Meta:
		unique_together = ('project', 'number',)

class PortType(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return '%s'% (self.name)
	
class Port(models.Model):
	number = models.CharField(max_length=200)
	type = models.ForeignKey(PortType)
	#device = models.ForeignKey('Door', through='DoorHardware', null=True, blank=True )
	controller = models.ForeignKey(Controller, null=True)
	
	def __str__(self):
		return 'Controller: %s - Type: %s - Port: %s'% (self.controller.number, self.type, self.number)
	