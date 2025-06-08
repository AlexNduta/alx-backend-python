from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['user-id', 'username', 'first_name', 'last_name', 'phone_number']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    class Meta;
        model=Conversation
        fields = '__all__'
