from django.db import models

class NetworkInfo(models.Model):
	ip = models.CharField(max_length=16, blank=True)
	subnet = models.CharField(max_length=16, blank=True)
	gateway = models.CharField(max_length=16, blank=True)
	vlan = models.CharField(max_length=200, blank=True)
	MAC = models.CharField(max_length=23, blank=True)
	
	def __str__(self):
		return '%s' % (self.ip)