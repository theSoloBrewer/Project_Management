from django.db import models
from apps.manufacturers.models import Manufacture
from apps.devices.models import Device

# Create your models here.

class Hardware(models.Model):
    manufacture = models.ForeignKey(Manufacture)
    type = models.ForeignKey(Device)
    model = models.CharField(max_length=200)
    
    
    def __str__(self):
        return '%s %s' % (self.manufacture, self.model)
    
