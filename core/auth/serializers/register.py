from rest_framework import serializers

from core.user.serializers import UserSerializers
from core.user.models import User


class RegisterSerializer(UserSerializers):
    """
    Registration serializer for requests and user creation
    """
    
    # Makin sure the password is at least 8 characters long, and not longer than 128 and can't be read
    # by the user
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True)
    
    class Meta:
        model = User
        # List of all the fileds that can ber included in a request or a response
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
        ]
        
    def create(self, validated_data):
        # Use the 'create_user method we wrote earlier for the User manager to create a new user
        return User.objects.create_user(**validated_data)
    