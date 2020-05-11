from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializers a name input to test our api view"""

    name = serializers.CharField(max_length=10)
