from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from GiKJiK.serializers import (ClassCreateSerializer, UserProfileCreateSerializer)

# Create your views here.

class UserProfileCreateView(generics.CreateAPIView):
    serializer_class = UserProfileCreateSerializer

    def perform_create(self, serializer):
        django_user = User.objects.create_user(username=self.request.get('username'), password=self.request.get('password'))
        serializer.save(django_user=django_user)

class ClassCreateView(generics.CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.user_profile)
