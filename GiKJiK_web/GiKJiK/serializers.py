from rest_framework import serializers
from GiKJiK.models import (News, Class, UserProfile)

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username',
                  'email',
                  'password', ]

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