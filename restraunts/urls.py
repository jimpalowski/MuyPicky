from django.conf.urls import url



from .views import (
	RestrauntListView,
	RestrauntDetailView,
 	RestrauntCreateView,
 	RestrauntUpdateView,
	)

urlpatterns = [
   url(r'^create/$', RestrauntCreateView.as_view(), name='create'),
   #url(r'^(?P<slug>[\w-]+)/edit/$', RestrauntUpdateView.as_view(), name='edit'),
   url(r'^(?P<slug>[\w-]+)/$', RestrauntUpdateView.as_view(), name='detail'),
   url(r'$', RestrauntListView.as_view(), name='list'),
]