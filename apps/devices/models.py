from django.db import models

# Create your models here.

class Device(models.Model):
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s' % (self.type)