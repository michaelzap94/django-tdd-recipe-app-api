from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
#our serializers class
from user.serializers import UserSerializer, AuthTokenSerializer

#generics.CreateAPIView -> view premade for us that will create a User object in the db using our serializer class
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    #override attribute from generics.CreateAPIView
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    #override attribute from ObtainAuthToken
    serializer_class = AuthTokenSerializer
    # (optional) sets the renderer UI so we can view A UI in the browser to create this object,
    #  otherwise we'll need Postman
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES