from django.shortcuts import render
from .models import *
from apps.cameras.models import *
from apps.home.views import formValidSave
from .forms import projectDetailsForm
from apps.doors.models import Door
from django.core.exceptions import ValidationError
from django.http import HttpResponse
# Create your views here.

def projectDetailsView(request, id=None):
	if id:
		obj = Project.objects.get(pk=id)
		door_list = Door.objects.all().filter(project_id=id).prefetch_related()
		camera_list = Camera.objects.filter(project_id=id).prefetch_related()
	else:
		obj = Project()
		door_list = []
		camera_list = []
	form = formValidSave(request, projectDetailsForm, obj, id)
	 
	return render(request, 'projects/details.html', {'form': form, 'door_list': door_list, 'camera_list': camera_list})
	
def projectDoorRemoveView(request):
	if request.method == 'POST':
		try:
			print request.POST['door_id']
			Door.objects.get(pk=request.POST['door_id']).delete()
			return HttpResponse(status=205)
		
		except ValidationError, e:
			return e.message_dict