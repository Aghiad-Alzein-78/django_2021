from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields='__all__'
        exclude=['votes_total','votes_ratio']
        widgets={
            'tags':forms.CheckboxSelectMultiple
        }
    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        self.fields['title'].widget.attrs.update({'class':'input','placeholder':"Add Title"})
        # self.fields['description'].widget.attrs.update({'class':'input'})
    

