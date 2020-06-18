from django.forms import ModelForm, TextInput, FileField, ClearableFileInput, DateInput, CheckboxInput, Textarea, Select
from .models import Attachment, Project

class AttachmentForm(ModelForm):
	class Meta:
		model = Attachment
		fields = ['name','project','file']

		widgets = {}
		for field in fields:
			if field == 'file':
				widgets[field] = ClearableFileInput(attrs={'label':'Select Logo:','multiple': True})
			else:
				widgets[field] = TextInput(attrs={'class':'form-control mr-sm-2', 'placeholder':field.capitalize()})

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'startdate', 'finished', 'finishdate', 'owner', 'description', 'status', 'language']                
        status_choices = (
            ('Not Started','Not Started'),
            ('Started','Started'),
            ('In Progress','In Progress'),
            ('Halted','Halted'),
            ('Finished','Finished')
        )

        language_choices = (
            ('Android','Android'),
            ('Angular','Angular'),
            ('C Shart','C Shart'),
            ('Django','Django'),
            ('Flask','Flask'),
            ('Flutter','Flutter'),
            ('Ionic','Ionic'),
            ('Java','Java'),
            ('Javascript','Javascript'),
            ('Kotlin','Kotlin'),
            ('Laravel','Laravel'),
            ('PHP','PHP'),
            ('Python','Python'),
            ('React','React'),
            ('VueJS','VueJS'),
            ('Yii','Yii')
        )        
        
        widgets = {'name':TextInput(attrs={'class':'form-control', 'required':True}),
                   'owner':TextInput(attrs={'class':'form-control', 'required':True}),
                   'description':Textarea(attrs={'class':'form-control', 'rows':2, 'placeholder':'Description', 'required':True}), 
                   'startdate':DateInput(attrs={'class':'form-control', 'required':True}), 
                   'status':Select(attrs={'class':'form-control', 'required':True}, choices=status_choices), 
                   'language':Select(attrs={'class':'form-control', 'required':True}, choices=language_choices),
                   'finishdate':DateInput(attrs={'class':'form-control', 'required':False}),
                   'finished':CheckboxInput(attrs={'class':'form-control inline-element', 'label':'Project Finished', 'required':False}),
                  }