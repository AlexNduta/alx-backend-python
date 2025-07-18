#from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from .pagination import MessagePagination
from .filters import MessageFilter
class ConversationViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allows for a conversation to be viewd or edited
    """

    # make a quey to the database to get all conversations
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # Show conversations to users who have been loggedin and authenticated
    permission_class = [permissions.IsAuthenticated, IsParticipantOfConversation]

    # enable filtering
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['participants'] # allow filtering conversations by participants ID

    def get_queryset(self):
        """
        ensure that users can only see their conversations
        """
        return self.request.user.conversations.all()
    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        """
        allows a user to leave a conversation
        """
        conversation = self.get_object()
        user = request.user
        if conversation.participants.count() == 1:
            return response.Response({
                'error': 'Cannot leave a conversation with only one participant'
                }, status=status.HTTP_403_FORBIDDEN)
        # if the check passes, remove user and return success
        conversation.paricipants.remove(user)
        return response.Response(
                {'status': 'You have left the conversation'},
                status=status.HTTP_200_OK
                )

class MessageViewSet(viewsets.ModelViewSet):
    """
    Api endpoint that allow for messages to be viewed or edited
    """

    # make a query to te database to get all Messages
   # queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessagePagination
    # ony show messages to users who have bee loggedin and authenticted
    permission_class = [IsParticipantOfConversation]
    #filter_backeds = 
    #  enable filtering
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['conversations', 'sender'] # allow filtering messages by sender
    filterset_class = MessageFilter
    def get_queryset(self):
        """
        ensure users only see messages of a convesation they are part of
        * We will filter the messages based on the conversation_pk from the nested URL
        """
        conversation_pk = self.kwargs['conversation_pk']
        return Message.objects.filter(conversation_id=conversation_pk)

    def perform_create(self, serializer):
        """
        * When creating a message, we automatically set the sender 
        to the logged-in user and associate it with the conversation from the URL
        """
        conversation_pk = self.kwargs['conversation_pk']
        conversation = Conversation.objects.get(pk=conversation_pk)
        serializer.save(sender=self.request.user, conversation=conversation)
