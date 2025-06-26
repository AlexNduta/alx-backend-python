from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filter

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from chats.permissions import IsParticipantOfConversation
from chats.pagination import MessagePagination
from chats.filters import MessageFilter
from .models import User, Conversation, Message
from .serializers import  UserSerializer, ConversationSerializer, MessageSerializer
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.contrib.auth import authenticate

class UserFilter(filter.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['iexact', 'icontains'],
            'email': ['iexact', 'icontains'],
            'date_joined': ['exact', 'gte', 'lte'],
        }

class ConversationFilter(filter.FilterSet):
    class Meta:
        model = Conversation
        fields = {
            'name': ['exact', 'icontains'],
            'created_at': ['exact', 'gte', 'lte'],
            'participants': ['exact'],
        }


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users in the messaging application.
    Provides CRUD operations for User model with authentication and filtering.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = UserFilter
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['username', 'email', 'date_joined']
    ordering = ['username']

    def get_permissions(self):
        """
        Custom permission handling:
        - Allow anyone to create a user (register)
        - Require authentication for updates/deletes
        - Allow read-only access for listing/retrieval
        """
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def create(self, request, *args, **kwargs):
        """
        Create a new user account (registration).
        Automatically generates an auth token for the new user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create token for the new user
        token, created = Token.objects.get_or_create(user=user)
        
        headers = self.get_success_headers(serializer.data)
        return Response({
            'user': serializer.data,
            'token': token.key
        }, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Update user information.
        Only allows users to update their own profile unless staff/superuser.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Ensure users can only edit their own profile unless they're staff
        if not request.user.is_staff and instance != request.user:
            return Response(
                {'detail': 'You can only edit your own profile.'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response(UserSerializer(user).data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a user account.
        Only allows users to delete their own account unless staff/superuser.
        """
        instance = self.get_object()
        
        # Ensure users can only delete their own account unless they're staff
        if not request.user.is_staff and instance != request.user:
            return Response(
                {'detail': 'You can only delete your own account.'},
                status=status.HTTP_403_FORBIDDEN
            )
            
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Custom delete handling - also deletes the auth token.
        """
        # Delete the user's token if it exists
        Token.objects.filter(user=instance).delete()
        instance.delete()

    def get_queryset(self):
        """
        Custom queryset handling:
        - Staff can see all users
        - Regular users can only see themselves in detail view
        - Everyone can see all users in list view (if permissions allow)
        """
        queryset = super().get_queryset()
        
        # For detail views, non-staff can only see themselves
        if self.action == 'retrieve' and not self.request.user.is_staff:
            return queryset.filter(pk=self.request.user.pk)
            
        return queryset

class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing conversations in the messaging application.
    Provides CRUD operations for Conversation model.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filter.DjangoFilterBackend]
    filterset_class = ConversationFilter
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        """
        Override the default queryset to filter conversations based on the authenticated user.
        """
        user = self.request.user
        if user.is_authenticated:
            return Conversation.objects.filter(participants=user)
        return Conversation.objects.none()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()
        return Response(ConversationSerializer(conversation).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        conversation = serializer.save()
        return Response(ConversationSerializer(conversation).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        """
        Delete the conversation instance.
        """
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        """
        List all conversations in the messaging application.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific conversation by ID.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_permissions(self):
        """
        Get the permissions for the ConversationViewSet.
        """
        if self.action in ['create', 'update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        """
        Get the serializer class for the ConversationViewSet.
        """
        if self.action in ['create', 'update']:
            return ConversationSerializer
        return ConversationSerializer
# class MessageViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet for managing messages in the messaging application.
#     Provides CRUD operations for Message model.
#     """
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     filter_backends = [filter.DjangoFilterBackend]
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsParticipantOfConversation]
#     filterset_class = MessageFilter
#     search_fields = ['message_body', 'sender__username', 'conversation__name']
#     ordering_fields = ['sent_at', 'sender__username']
#     ordering = ['-sent_at']
#     def get_queryset(self):
#         """
#         Override the default queryset to filter messages based on:
#         - Authenticated user's conversations
#         - Optional conversation_id parameter
#         """
#         queryset = super().get_queryset()
#         user = self.request.user
        
#         if user.is_authenticated:
#             # Get conversation_id from query params if available
#             conversation_id = self.request.query_params.get('conversations_id')
            
#             if conversation_id:
#                 print(f"Filtering messages for conversation_id: {conversation_id}")
#                 # Filter messages for specific conversation where user is participant
#                 queryset = Message.objects.filter(
#                     conversations__id=conversation_id,
#                     conversations__participants=user
#                 )
#             else:
#                 # Filter all messages from conversations where user is participant
#                 queryset = Message.objects.filter(
#                     conversations__participants=user
#                 )
#         else:
#             queryset = Message.objects.none()
            
#         return queryset
class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    filter_backends = [filter.DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAuthenticatedOrReadOnly, IsParticipantOfConversation]
    filterset_class = MessageFilter
    search_fields = ['message_body', 'sender__username', 'conversation__name']
    ordering_fields = ['sent_at', 'sender__username']
    ordering = ['-sent_at']
    parent_lookup_field = 'conversation_id' 
    pagination_class = MessagePagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Message.objects.none()
            
        # For nested routes (conversation/messages/)
        if 'conversation_pk' in self.kwargs:
            return Message.objects.filter(
                conversation_id=self.kwargs['conversation_pk'],
                conversation__participants=user
            ).select_related('sender', 'conversation')
            
        # For standalone messages endpoint
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(
                conversation_id=conversation_id,
                conversation__participants=user
            ).select_related('sender', 'conversation')
            
        # All messages from user's conversations
        return Message.objects.filter(
            conversation__participants=user
        ).select_related('sender', 'conversation')

    def perform_create(self, serializer):
        # For nested routes
        if 'conversation_pk' in self.kwargs:
            conversation = get_object_or_404(
                Conversation,
                pk=self.kwargs['conversation_pk'],
                participants=self.request.user
            )
            serializer.save(sender=self.request.user, conversation=conversation)
        else:
            # For standalone endpoint
            conversation_id = serializer.validated_data.get('conversation_id')
            conversation = get_object_or_404(
                Conversation,
                pk=conversation_id,
                participants=self.request.user
            )
            serializer.save(sender=self.request.user, conversation=conversation)
            