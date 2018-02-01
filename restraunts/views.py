from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import RestrauntLocation

def restraunt_listview(request):
	template_name = 'restraunts/restraunts_list.html'
	queryset = RestrauntLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)


