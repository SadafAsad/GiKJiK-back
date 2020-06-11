from rest_framework import serializers
from GiKJiK.models import (News, Class, UserProfile)
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password', ]

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['pk', 'name', 'class_id', ]
        # extra_kwargs = {'owner': {'read_only': True}}

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['pk', '_classes', 'title', 'description', 'date']

# sign up kardan --> username, email, password