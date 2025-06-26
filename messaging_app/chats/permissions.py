from rest_framework import permissions

from .models import Conversation
# Import typing for type annotations to enhance code clarity
from typing import Optional
from rest_framework.request import Request
from rest_framework.views import View

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """
    
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
            
        # For list/create actions, check if they're trying to access a conversation they're in
        if view.action in ['list', 'create']:
            # For nested messages creation
            if 'conversation_pk' in view.kwargs:
                conversation_id = view.kwargs['conversation_pk']
                return Conversation.objects.filter(
                    conversation_id=conversation_id,
                    participants=request.user
                ).exists()
            return True  # Allow listing messages with filters
            
        # For other actions, rely on has_object_permission
        return True
    def has_object_permission(self, request: Request, view: View, obj: Conversation) -> bool:
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Allow all participants for safe methods
        if request.method in permissions.SAFE_METHODS:
            return obj.participants.filter(user_id=request.user.id).exists()
        
        # For PUT, PATCH, DELETE, check if user is participant
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.participants.filter(user_id=request.user.id).exists()
        
        return False