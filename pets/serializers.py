from rest_framework import serializers
from .models import SexChoices
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class SexSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    sex = serializers.ChoiceField(
        choices=SexChoices.choices, default=SexChoices.INFORMED
    )


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=SexChoices.choices, default=SexChoices.INFORMED)
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
