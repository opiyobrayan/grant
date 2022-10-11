from django import forms
from .models import Grant

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model=Grant
        fields='__all__'


