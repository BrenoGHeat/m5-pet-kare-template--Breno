from rest_framework import serializers


class GroupSerializers(serializers.Serializer):
    scientific_name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True) 