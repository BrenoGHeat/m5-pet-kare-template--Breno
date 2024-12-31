from rest_framework import serializers


class TraitSerializer():
    trait_name = serializers.CharField(source="name")
    created_at = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)
