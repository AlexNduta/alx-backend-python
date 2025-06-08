from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet


# create a router and register our viewset with it
router = DefaultRouter()
router.register(r'conversation', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')


urlpatterns =[
        path('', include(router.urls))
        ]
