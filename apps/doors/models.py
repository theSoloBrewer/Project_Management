from django.db import models
from apps.hardware.models import Hardware
from apps.projects.models import Project
from apps.controllers.models import Port
# Create your models here.
class Door(models.Model):
	project = models.ForeignKey(Project)
	devices = models.ManyToManyField(Hardware, through='DoorHardware', symmetrical=False)
	number = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200, blank=True)
	notes = models.TextField(blank=True)
	
	def __str__(self):
		return '%s %s' % (self.number, self.name)
	
class DoorHardware(models.Model):
	
	door = models.ForeignKey(Door)
	hardware = models.ForeignKey(Hardware)
	port = models.ForeignKey(Port, null=True, blank=True)
	
	installed = models.BooleanField(default=False)
	# port = models.ForeignKey(Controller)
	
	def __str__(self):
		return '%s' % (self.hardware)