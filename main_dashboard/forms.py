from django import forms
from .models import Grant

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model=Grant
        fields='__all__'



from .models import Participant

class PersonData(forms.Form):
	class meta:
		model = Participant
		fields = '__all__'