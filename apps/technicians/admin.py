from django.contrib import admin
from .models import *
# Register your models here.

class technicianAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'phone')
    
#class techMemberAdmin(admin.ModelAdmin):
    
    
admin.site.register(technician, technicianAdmin)
# admin.site.register(technicianMember)