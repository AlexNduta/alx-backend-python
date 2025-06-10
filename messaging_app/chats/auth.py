from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairview


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        """
        call this method to generate the token
        - First get token from the super class
        """
        # get the standard token and with its default claims
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class MyTokenObtainPairView(TokenObtainPairview):
    """
    tell the view to use out new custom serializer
    """
    serializer_class = MyTokenObtainPairSerializer
