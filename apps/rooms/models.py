from django.db import models
from apps.hardware.models import Hardware
from apps.projects.models import Project
# Create your models here.
class Room(models.Model):
	project = models.ForeignKey(Project)
	devices = models.ManyToManyField(Hardware, through='RoomHardware', symmetrical=False)
	number = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200, blank=True)
	notes = models.TextField(blank=True)
	
	def __str__(self):
		return '%s %s' % (self.number, self.name)
	
class RoomHardware(models.Model):
	
	room = models.ForeignKey(Room)
	hardware = models.ForeignKey(Hardware)
	
	installed = models.BooleanField(default=False)
	serial = models.CharField(max_length=200, blank=True)
	#port = models.ForeignKey(Controller)
	
	def __str__(self):
		return '%s' % (self.hardware)