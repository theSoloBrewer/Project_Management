from django.db import models
from apps.projects.models import Project

# Create your models here.
class technician(models.Model):
    # members = models.ManyToManyField(Project, through='technicianMember')
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return '%s %s' % (self.fname, self.lname)
    
# class technicianMember(models.Model):
    # project = models.ForeignKey(project)
    # tech = models.ForeignKey(technician)
    # hours = models.IntegerField()
    
    # def __str__(self):
        # return '%s' % (self.tech)
    