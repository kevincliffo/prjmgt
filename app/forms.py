from django.forms import ModelForm, TextInput, FileField, ClearableFileInput
from .models import Attachment

class AttachmentForm(ModelForm):
	class Meta:
		model = Attachment
		fields = ['name','project','file']

		widgets = {}
		for field in fields:
			if field == 'file':
				widgets[field] = ClearableFileInput(attrs={'label':'Select Logo:','multiple': True})
                #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'label':'Select Logo:','multiple': True}))
			else:
				widgets[field] = TextInput(attrs={'class':'form-control mr-sm-2', 'placeholder':field.capitalize()})
