from django.urls import include, path, re_path
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Create nested router
conversations_router = routers.NestedDefaultRouter(
    router, 
    r'conversations', 
    lookup='conversation'
)
conversations_router.register(
    r'messages', 
    MessageViewSet, 
    basename='conversation-messages'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversations_router.urls)),
    re_path(r'auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
]