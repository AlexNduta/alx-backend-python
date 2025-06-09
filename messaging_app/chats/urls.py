from django.urls import path, include 
from rest_framework import routers 
from .views import ConversationViewSet, MessageViewSet


# create a router and register our viewset with it
# viewsets are what we imported from `views.py` in this case Conversationviewset and MessageViewset
router = routers.DefaultRouter()
# register the routes to generate URL patterns
# router.register(prefix, viewset, basename[optional])
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')
"""
URLs generated will be conversation/, conversation/<id>/ and messages/, messages/<id>/
"""

urlpatterns =[
        path('', include(router.urls))
        ]
