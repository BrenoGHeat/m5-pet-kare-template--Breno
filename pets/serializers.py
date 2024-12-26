from rest_framework import serializers
from .models import SexChoices


class SexSerializer(serializers.Serializer):
    name = serializers.CharField(max_lenght=20)
    sex = serializers.ChoiceField(
        choices=SexChoices.choices, default=SexChoices.INFORMED
    )
