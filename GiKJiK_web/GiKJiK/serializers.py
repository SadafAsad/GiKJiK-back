from rest_framework import serializers
from GiKJiK.models import (News, Class, UserProfile)
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password', ]
    
    def validate_password(self, value: str) -> str:
        return make_password(value)

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name', 'class_id', ]

class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
