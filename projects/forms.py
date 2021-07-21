from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields='__all__'
        exclude=['votes_total','votes_ratio']


