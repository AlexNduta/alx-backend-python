from django.urls import path, include
# import the nested routre
from rest_framework_nested import routers 
from .views import ConversationViewSet, MessageViewSet


# create a router and register our viewset with it
# viewsets are what we imported from `views.py` in this case Conversationviewset and MessageViewset
router = routers.DefaultRouter()
# register the routes to generate URL patterns
# router.register(prefix, viewset, basename[optional])
# Our main router will be the conversation
router.register(r'conversations', ConversationViewSet, basename='conversation')

# we create a nested router
# The nested router depends on the main router with the conversation prefix
conversation_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
# Register the MessageViewset on the nested router
# This will create a URL like /conversations/{conversation_pk}/messages/
conversation_router.register(r'messages', MessageViewset, basename='conversation-messages')
"""
URLs generated will be conversation/, conversation/<id>/ and messages/, messages/<id>/
"""

urlpatterns =[
        path('', include(router.urls))
        path('', include(conversation_router.urls))
        
        ]
