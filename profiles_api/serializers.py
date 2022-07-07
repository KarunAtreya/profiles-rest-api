from unicodedata import name
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIview"""
    name = serializers.CharField(max_length=10)

    


