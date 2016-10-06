from django.contrib import admin
from .models import *
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('job_code', 'title')
    
admin.site.register(Project, ProjectAdmin)