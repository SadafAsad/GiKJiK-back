from django.shortcuts import render
from rest_framework import generics
from GiKJiK.models import UserProfile, Class
from GiKJiK.serializers import *

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
        serializer.save(owner=self.request.user.user_profile)

class ClassListView(generics.ListAPIView):
    serializer_class = ClassListSerializer

    def get_queryset(self):
        return Class.objects.all()
    
