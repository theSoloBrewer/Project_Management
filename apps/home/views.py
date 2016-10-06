from django.shortcuts import render,render_to_response
from .forms import welcomePageForm 
from apps.projects.models import Project 
from django.http import HttpResponseRedirect

# Create your views here.
def welcomePageView(request):
	form = welcomePageForm()
	list = Project.objects.all()
	if request.method == 'POST':
		form = welcomePageForm(request.POST)
		if form.is_valid():
			project_id = request.POST['projects']
			return HttpResponseRedirect('/projects/' + project_id)

	 
	return render(request, 'base.html', {'form': form, 'list': list})
	
	
def formValidSave(request,TargetForm,TargetInstance,id=None):
	form = TargetForm(instance=TargetInstance)
	if request.method == 'POST':
		form = TargetForm(request.POST,instance=TargetInstance)
		if form.is_valid():
				form.cleaned_data = request.POST
				m = form.save()
		print(form.errors)
				
	return form
