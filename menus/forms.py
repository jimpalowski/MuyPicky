from django import forms


from restraunts.models import RestrauntLocation


from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'restraunt',
			'name',
			'contents',
			'excludes',
			'public',
		]

	def __init__(self, user=None, *args, **kwargs):
		#print(kwargs.pop('user'))
		print(user)
		print(kwargs)
		super(ItemForm, self).__init__(*args,**kwargs)
		self.fields['restraunt'].queryset = RestrauntLocation.objects.filter(owner=user)#.exclude(item__isnull=False)