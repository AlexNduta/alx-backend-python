from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    This is a custom permission check for:
          1. If the user is authenticated
          2. if the user is a participant of a conversation they are trying to accessB[

    """

    def has_permission(self, request, view):
        """ first check to confirm a user is logged in for any requests
        - This will be called first so that we can know that a user is authenticated
        """
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        This method is called for detailed views 
        'obj' is the instance of the conversation or message
        """
        # check for object-level permissions
        if request.method in permissions.SAFE_METHODS:
            # check permission for read-only
            pass
        else:
            # check permission for write request (PUT, PATCH, DELETE)
            pass


        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()

        if hasattr(obj, 'conversation'):
            return request.user  in obj.conversation.participants.all()
        return false

