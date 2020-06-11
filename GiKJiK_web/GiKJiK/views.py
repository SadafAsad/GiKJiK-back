from django.shortcuts import render
from rest_framework import generics
from GiKJiK.models import UserProfile
from GiKJiK.serializers import (ClassCreateSerializer, UserCreateSerializer, UserProfileListSerializer)

class SignUpView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserProfileListView(generics.ListAPIView):
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.all()

class ClassCreateView(generics.CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
