from django.shortcuts import render
from rest_framework import generics
from GiKJiK.serializers import (ClassCreateSerializer)

# Create your views here.
class ClassCreateView(generics.CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.user_profile)
