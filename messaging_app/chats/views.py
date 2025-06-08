#from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows for a conversation to be viewd or edited
    """

    # make a quey to the database to get all conversations
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # Show conversations to users who have been loggedin and authenticated
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        ensure that users can only see their conversations
        """
        return self.request.user.conversations.all()
class MessageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allow for messages to be viewed or edited
    """

    # make a query to te database to get all Messages
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # ony show messages to users who have bee loggedin and authenticted
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        ensure users only see messages of a convesation they are part of
        """
        return Message.objects.filter(conversation__in=user_conversations)
