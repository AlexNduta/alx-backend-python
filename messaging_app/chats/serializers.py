from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'phone_number']

class MessageSerializer(serializers.ModelSerializer):
   sender = serializers.StringRelatedField(read_only=True)

   class Meta:
        model=Message
        exclude = ['conversation']

class ConversationSerializer(serializers.ModelSerializer):
  """
  - we have three 'magic fields':
    participants_info
    message_count
    latest_message

    ------
    - DRF knows that, to get the value of the participants_info, it must call the method, get_partcipants_info()
    - 

  """
    # custom conversation  fields
    conversation_summary = serializers.CharField(source='__str__', read_only=True)

    # 'magic' fields related to serializerMethods

    participants_info= serializers.SerializerMethodField()
    message_count = serializers.SerializerMethodField()
    latest_message = serializers.SerializerMethodField()

    class Meta:
        model=Conversation
        fields = ['conversation_id', 
                  'conversation_summary', #our character field
                  'participants_info',  # our first serilizermathodfied;
                  'message_count',      # our second serializermethodfield
                  'latest_message', # Our 3rd serialiser method field
                  ]
    def get_participants_info(self, obj):
        """
        *This method is automatically called by DRF to populate paricipants info
        * we get all the participants and serialize them with UserSerializer
        - The obj is the conversation instance object to serialize
        - 
        """
        participants = obj.participants.all()
        return UserSerializer(participants, many=True).data

    def get_message_count(self, obj):
        """
        * polulates the 'message_count'
        * we use the related name 'messages' to count messages
        """
        return obj.messages.count()
    
    def get_latest_message(self, obj):
        """populates the 'latest_message' """
        latest = obj.messages.order_by('-created_at').first()
        if latest:
            # use MessageSerializer to format the latest message
            return  MessageSerializer(latest).data
        return None # return nothing if there are no messages

    def validate(self, data):
        """ This is a validation for creating/updating conversation 
        * Demonstrates the use of serializers.ValidationError
        """
        # when creating a conversation, partcipants must be provided
        participants = self.initial_data.get('participants', [])

        if len(participants) < 2:
            raise serializers.ValidationError("A conversation must have atleast two participants")
        return data

