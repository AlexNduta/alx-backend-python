from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'phone_number']

class MessageSerializer(serializers.ModelSerializer):
   sender = UserSerializer(read_only=True)# create an instance of the sender's info that we will use

   class Meta:
        model=Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    # 
    participants= UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model=Conversation
        fields = ['conversation_id', 'participants', 'messages']
