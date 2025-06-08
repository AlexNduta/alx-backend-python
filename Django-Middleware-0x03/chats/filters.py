from django_filters import rest_framework as filter
from chats.models import Message

class MessageFilter(filter.FilterSet):
    class Meta:
        model = Message
        fields = {
            'message_body': ['exact', 'icontains'],
            'sent_at': ['exact', 'gte', 'lte'],
            'sender': ['exact'],
        }
