from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from.forms import RestrauntCreateForm, RestrauntLocationCreateForm
from .models import RestrauntLocation



class RestrauntListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return	RestrauntLocation.objects.filter(owner=self.request.user)	
	

class RestrauntDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return	RestrauntLocation.objects.filter(owner=self.request.user)	

class RestrauntCreateView(LoginRequiredMixin, CreateView):
	form_class = RestrauntLocationCreateForm
	login_url = '/login/'
	template_name = 'form.html'
	#success_url = "/restraunts/"


	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestrauntCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestrauntCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restraunt'
		return context 


class RestrauntUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestrauntLocationCreateForm
	login_url = '/login/'
	template_name = 'restraunts/detail-update.html'
	#success_url = "/restraunts/"


	def get_context_data(self, *args, **kwargs):
		context = super(RestrauntUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = f'Update Restraunt: {name}'
		return context 

	def get_queryset(self):
		return	RestrauntLocation.objects.filter(owner=self.request.user)





