from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Task

def validate_title(value):
    if value.lower() in ['hello', 'world', 'example', 'invalid', 'forbidden', 'restricted', 'disallowed']:
        raise serializers.ValidationError(f"{value} is not allowed")
    return value

Unique = UniqueValidator(queryset=Task.objects.all(), lookup='iexact', message="Title must be unique.")