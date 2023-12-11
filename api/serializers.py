from rest_framework import serializers
from .models import Todo, User
from .validators import validate_title, Unique

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)

class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_title, Unique])
    class Meta:
        model = Todo
        fields = [
            'id',
            'user',
            'title',
            'description',
            'completed',
            'priority',
            'url',
            'created_at',
            'updated_at',
        ]

    def get_url(self, obj):
        return f"/api/todo/{obj.id}/"