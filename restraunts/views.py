from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView



from.forms import RestrauntCreateForm
from .models import RestrauntLocation


def restraunt_createview(request):
	if request.method == "GET":
		print("get data")
	if request.method == "POST":
		print("post data")
		print(request.POST)	
	template_name = 'restraunts/form.html'
	context = {}
	return render(request, template_name, context)




def restraunt_listview(request):
	template_name = 'restraunts/restrauntlocation_list.html'
	queryset = RestrauntLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)


def restraunt_detailview(request, slug):
	template_name = 'restraunts/restraunts_detail.html'
	obj = RestrauntLocation.objects.get(slug=slug)
	context = {
		"object": obj
	}
	return render(request, template_name, context)





class RestrauntListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestrauntLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
				)
		else:
			queryset = RestrauntLocation.objects.all()	
		return queryset




class RestrauntDetailView(DetailView):
	queryset = RestrauntLocation.objects.all()#filter(category__iexact='asian')

	'''def get_object(self, *args, **kwargs):
		rest_id = self.kwargs.get('rest_id')
		obj = get_object_or_404(RestrauntLocation, id=rest_id)
		return obj 

'''


