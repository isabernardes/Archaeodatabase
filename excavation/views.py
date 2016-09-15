from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

#def excavation_create():

def excavation_list(request):
	queryset = Grabung.objects.all()
	context = {
		"object_list": queryset

	}
	return render(request, 'homepage.html', context)

def excavation_detail(request, id=None):
	instance = get_object_or_404(Grabung, id=id)
	queryset = Befund.objects.filter(ausgrabung=id)
	context = {
	"list": queryset,
	"instance":instance,

	}
	return render(request, 'excavation_detail.html',context)

#def befund_create():



#def befund_detail():

#def befund_update():

#def photos_list():

#def delete():
