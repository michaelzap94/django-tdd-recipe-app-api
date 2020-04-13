from django.contrib.auth import get_user_model, authenticate
#it will translate into diff languages if we want to later
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

#1 call create function using validated_data
#2 validated_data will contain all data passed into the serializer(Meta) (JSON data in the HTTP post BODY)
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""
    #Override from rest_framework
    class Meta:
        model = get_user_model()
        #fields we want to make accessible in the API.
        #fields that will be converted to and from JSON
        fields = ('email', 'password', 'name')
        #extra settings in the serializer
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    #Override from rest_framework
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    # Override from rest_framework
    # we need to make sure the password is using the set_password function that encrypts it.
    # we don't need this for create as "create_user" will use it by default
    def update(self, instance, validated_data):
        #instance will be the model object instance, User Object
        #validated_data the fields we specified above
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)#pop the password
        user = super().update(instance, validated_data)#run the update on the model using the new data

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    #override the Serializer attrs
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        #attrs every field we override in the serializer(look UP )
        email = attrs.get('email')
        password = attrs.get('password')

        #USE THE rest_framework authenticate function
        user = authenticate(
            request=self.context.get('request'), # gets the request obj passed from the views
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs    