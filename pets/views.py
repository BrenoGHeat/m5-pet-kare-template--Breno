from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pets.models import Pet
from pets.serializers import PetSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class PetView(APIView, PageNumberPagination):
    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pet = Pet.objects.create(**serializer.validated_data)
        serializer = PetSerializer(pet)

        return Response(serializer.data, 201)

    def get(self, request):
        pets = Pet.objects.all()
        result_page = self.paginate_queryset(pets, request, view=self)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
