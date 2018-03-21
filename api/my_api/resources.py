from tastypie.resources import ModelResource
from my_api.models import Note


class NoteResource(ModelResource):
	class Meta:
		queryset = Note.objects.all()
		resource_name = 'note'