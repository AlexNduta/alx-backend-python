import django_filters
from .models import Message


class MessageFilter(django_filters.FilterSet):
    """ search messages on a certain criteria """

    # create filter for a search date
    start_date  = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')


    # create a filter for an end date
    end_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'conversation']
