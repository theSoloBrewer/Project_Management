from django.shortcuts import render
from .forms import *

# Create your views here.
def manufactureDetailsView(request, mid=None):
    form = manufactureDetailsForm()
    if request.method == 'POST':
        form = manufactureDetailsForm(request.POST)
        if form.is_valid():
            manufacture_id = request.POST['manufacture']
            return HttpResponseRedirect('/manufacture/' + manufacture_id)

    else:
        if(mid!=None):
            mObj = Manufacture.objects.get(pk=mid)
            form = manufactureDetailsForm(instance=mObj)

    return render(request, 'manufacturers/details.html', {'form': form})