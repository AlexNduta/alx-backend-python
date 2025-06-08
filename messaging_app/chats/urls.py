from django.urls import path, include 
from rest_framework import routers 
from .views import ConversationViewSet, MessageViewSet


# create a router and register our viewset with it
router = routers.DefaultRouter()
router.register(r'conversation', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')


urlpatterns =[
        path('', include(router.urls))
        ]
