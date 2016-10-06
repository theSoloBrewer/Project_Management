from django.db import models
from apps.projects.models import Project
from apps.hardware.models import Hardware
from apps.common import *
from apps.manufacturers.models import Manufacture

# Create your models here.

class Camera(models.Model):
	project = models.ForeignKey(Project)
	name = models.CharField(max_length=200)
	device = models.ForeignKey(Hardware, null=False, blank=False, default='')
	installed = models.BooleanField(default=False)
	serial = models.CharField(max_length=200, blank=True)
	network = models.OneToOneField(NetworkInfo, null=True, blank=True, on_delete=models.SET_NULL)
	description = models.CharField(max_length=200, blank=True)
	notes = models.TextField(blank=True)
	
	def __str__(self):
		return '%s %s' % (self.name, self.device)