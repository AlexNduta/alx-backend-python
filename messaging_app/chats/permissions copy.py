from rest_framework import permissions


class IsChatParticipant(permissions.BasePermission):
    """
    Custom permission to only allow participants of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a participant of the chat
        return request.user in chat.participants.all()
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a participant of the chat
        return request.user in obj.participants.all()
class IsChatOwner(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is the owner of the chat
        return chat.owner == request.user
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is the owner of the chat
        return obj.owner == request.user
class IsChatAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is an admin of the chat
        return request.user in chat.admins.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is an admin of the chat
        return request.user in obj.admins.all()
class IsConversationParticipant(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the conversation from the view's kwargs
        conversation = view.get_object()
        
        # Check if the user is a member of the conversation
        return request.user in conversation.participants.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a member of the conversation
        return request.user in obj.members.all()

class IsChatMember(permissions.BasePermission):
    """
    Custom permission to only allow members of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a member of the chat
        return request.user in chat.members.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a member of the chat
        return request.user in obj.members.all()
class IsChatModerator(permissions.BasePermission):
    """
    Custom permission to only allow moderators of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a moderator of the chat
        return request.user in chat.moderators.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a moderator of the chat
        return request.user in obj.moderators.all()
class IsChatGuest(permissions.BasePermission):
    """
    Custom permission to only allow guests of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a guest of the chat
        return request.user in chat.guests.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a guest of the chat
        return request.user in obj.guests.all()
class IsChatViewer(permissions.BasePermission):
    """
    Custom permission to only allow viewers of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a viewer of the chat
        return request.user in chat.viewers.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a viewer of the chat
        return request.user in obj.viewers.all()
class IsChatSubscriber(permissions.BasePermission):
    """
    Custom permission to only allow subscribers of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a subscriber of the chat
        return request.user in chat.subscribers.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a subscriber of the chat
        return request.user in obj.subscribers.all()
class IsChatFollower(permissions.BasePermission):
    """
    Custom permission to only allow followers of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a follower of the chat
        return request.user in chat.followers.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a follower of the chat
        return request.user in obj.followers.all()
class IsChatContributor(permissions.BasePermission):
    """
    Custom permission to only allow contributors of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a contributor of the chat
        return request.user in chat.contributors.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a contributor of the chat
        return request.user in obj.contributors.all()
class IsChatCollaborator(permissions.BasePermission):
    """
    Custom permission to only allow collaborators of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a collaborator of the chat
        return request.user in chat.collaborators.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a collaborator of the chat
        return request.user in obj.collaborators.all()
class IsChatListener(permissions.BasePermission):
    """
    Custom permission to only allow listeners of a chat to access it.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Get the chat from the view's kwargs
        chat = view.get_object()
        
        # Check if the user is a listener of the chat
        return request.user in chat.listeners.all()
    
    def has_object_permission(self, request, view, obj):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a listener of the chat
        return request.user in obj.listeners.all()