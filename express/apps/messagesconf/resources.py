from import_export import resources
from .models import MessagesList

class MessagesListResource(resources.ModelResource):
    class Meta:
        model = MessagesList
        fields = ('id','name', 'phone')
        