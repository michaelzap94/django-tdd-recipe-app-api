from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag

from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,) # requires that token auth is used
    permission_classes = (IsAuthenticated,)# requires User is authenticated
    queryset = Tag.objects.all() # query to be run
    serializer_class = serializers.TagSerializer # serializer to be used

    # OVERRIDE get_queryset function that will be called to run THE :queryset = Tag.objects.all() (ABOVE)
    # THIS WAY, we can add filtering,  to the self.queryset that we retrieved ABOVE
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    # OVERRIDE perform_create function that will be called when CREATING/Adding an Object/Model to the db
    # serializer - object passed from the serializer Meta
    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)