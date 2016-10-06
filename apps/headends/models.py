from django.db import models
from apps.hardware.models import Hardware

# Create your models here.
class HeadEnd(models.Model):
	location = models.CharField(max_length=200)
	equipment = models.ManyToManyField(Hardware, through='Equipment', symmetrical=False)
	
	
class Equipment(models.Model):
	headend = models.ForeignKey(HeadEnd)
	device = models.ForeignKey(Hardware)
	ip_address = models.CharField(max_length=16)
	subnet = models.CharField(max_length=16)
	gateway = models.CharField(max_length=16)
	