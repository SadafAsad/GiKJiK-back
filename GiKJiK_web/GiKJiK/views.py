from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from GiKJiK.serializers import (ClassCreateSerializer, UserProfileCreateSerializer)

# Create your views here.

class UserProfileCreateView(generics.CreateAPIView):
    serializer_class = UserProfileCr`eateSerializer

    def perform_create(self, serializer):
        serializer_class.save()

class ClassCreateView(generics.CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.user_profile)
