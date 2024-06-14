from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogList(APIView):
    """Список всех собак или создать новый экземпляр собаки"""

    def get(self, request, format=None):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """Получить, изменить или удалить экземпляр собаки"""

    def get(self, request, pk, format=None):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedDetail(viewsets.ViewSet):
    """Получить, изменить или удалить экземпляр породы"""

    def retrieve(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def update(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)

        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)
        breed.delete()
        return Response(status=204)


class BreedList(viewsets.ViewSet):
    """Получить все породы или добавить один новый экземпляр"""

    def list(self, request):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
