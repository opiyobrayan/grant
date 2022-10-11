from import_export import resources
from .models import Participant

class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant