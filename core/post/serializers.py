from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='public_id'
    )
    
    def validate(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't a post for other user.")
        return value
    
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'body',
            'edited',
            'created',
            'updated',
        )
        
        read_only_fields = ['edited']
        
    def to_representation(self, instance):
        rep = seper().to_representation(instance)
        author = User.objects.get_by_natural_key(
            rep['author'])
        rep['author'] = UserSerializer(author).data
        
        return rep       