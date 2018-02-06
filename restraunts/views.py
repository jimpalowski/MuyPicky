from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView



from.forms import RestrauntCreateForm, RestrauntLocationCreateForm
from .models import RestrauntLocation


def restraunt_createview(request):
	form = RestrauntLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
		 	instance = form.save(commit=False)


		 	instance.owner = request.user
		 	form.save() 
		 	return HttpResponseRedirect("/restraunts/")
		else:
			return HttpResponseRedirect("/login/")
	if form.errors: 
		errors = form.errors

	template_name = 'restraunts/form.html'
	context = {"form": form , "errors": errors}
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
	queryset = RestrauntLocation.objects.all()

class RestrauntCreateView(CreateView):
	form_class = RestrauntLocationCreateForm
	template_name = 'restraunts/form.html'
	success_url = "/restraunts/"


	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestrauntCreateView, self).form_valid(form)










