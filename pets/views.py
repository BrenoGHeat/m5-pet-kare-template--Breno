from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from pets.models import Pet
from pets.serializers import PetSerializer
from rest_framework.pagination import PageNumberPagination
from groups.models import Group
from traits.models import Trait
# Create your views here.


class PetView(APIView, PageNumberPagination):
    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pet = serializer.validated_data
        group = pet.pop("group")
        traits = pet.pop("traits")
        group_find = Group.objects.filter(scientific_name=group["scientific_name"]).first()
        if not group_find:
            group_find = Group.objects.create(**group)
        pet = Pet.objects.create(**pet, group=group_find)
        traits_obj = []
        for trait in traits:
            trait_find = Trait.objects.filter(name__iexact=trait["name"]).first()
            if not trait_find:
                trait_find = Trait.objects.create(**trait)
            traits_obj.append(trait_find)

        pet.traits.set(traits_obj)
        serializer = PetSerializer(pet)

        return Response(serializer.data, 201)

    def get(self, request):
        if request.query_params:
            trait = request.query_params.get("trait", None)
            pets = Pet.objects.filter(
                traits__name=trait,
            )
        else:
            pets = Pet.objects.all()

        result_page = self.paginate_queryset(pets, request, view=self)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class PetDetailView(APIView):
    def delete(self, request, pet_id: int):
        try:
            pet = Pet.objects.get(id=pet_id)

        except Exception:
            return Response({"detail": "Not found."}, 404)
        pet.delete()

        return Response(status=204)

    def get(self, request, pet_id: int):

        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data, 200)

    def patch(self, request, pet_id: int):

        try:
            pet = Pet.objects.get(id=pet_id)

        except Exception:
            return Response({"detail": "Not found."}, 404)
        serializer = PetSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        pet_body = serializer.validated_data

        if "group" in pet_body:
            group = pet_body.pop("group")
            group_find = Group.objects.filter(scientific_name=group["scientific_name"]).first()
            if not group_find:
                group_find = Group.objects.create(**group)
            pet.group = group_find

        if "traits" in pet_body:
            traits = pet_body.pop("traits")
            traits_obj = []
            for trait in traits:
                trait_find = Trait.objects.filter(name__iexact=trait["name"]).first()
                if not trait_find:
                    trait_find = Trait.objects.create(**trait)
                traits_obj.append(trait_find)
            pet.traits.set(traits_obj)
        for key, value in pet_body.items():
            if key != "id":
                setattr(pet, key, value)
        pet.save()
        serializer = PetSerializer(pet)
        return Response(serializer.data, 200)
