from django.db import models

# Create your models here.
class Project(models.Model):
	job_code = models.CharField(max_length=6)
	title = models.CharField(max_length=200)
	comments = models.TextField(blank=True)
	lat = models.DecimalField (max_digits=8, decimal_places=3, blank=True, null=True)
	lng = models.DecimalField (max_digits=8, decimal_places=3, blank=True, null=True)

	
	def __unicode__(self):
		return '%s %s' % (self.job_code, self.title)
