from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    This is a custom permission to allow only participans of a conversation to view it
    """
    def has_object_permission(self, request, view, obj):
        """
        This method is called for detailed views 
        'obj' is the instance of the conversation or message
        """
        if isinstance(obj, conversation):
            return request.user in obj.participants.all()

        if hasattr(obj, 'conversation'):
            return request.user  in obj.conversation.participants.all()
        return false

