from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from restraunts.models import RestrauntLocation

class Item(models.Model):
	user 				= models.ForeignKey(settings.AUTH_USER_MODEL)
	restraunt 			= models.ForeignKey(RestrauntLocation)

	name				= models.CharField(max_length=120)
	contents			= models.TextField(help_text='Separate each item by comma')
	excludes			= models.TextField(blank=True, null=True, help_text='Separate each item by comma')
	public				= models.BooleanField(default=True)
	timestamp           = models.DateTimeField(auto_now_add=True)
	updated             = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name



	def get_absolute_url(self):
		#return f"/restraunts/{self.slug}"
		return reverse('menus:detail', kwargs={'pk': self.pk})


	class Meta:
		ordering = ['-updated', '-timestamp']


	def get_contents(self):
		return self.contents.split(",")

	def get_excludes(self):
		return self.excludes.split(",")