from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from .serializers import CarDetailSerializer
from .models import Car

class CreateCarView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    permission_classes = [permissions.IsAuthenticated]



class ListCarView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    permission_classes = [permissions.IsAuthenticated|permissions.IsAdminUser]
    

    

    

    

    

    

    
