from rest_framework import serializers
from django.contrib.auth.models import User
from GiKJiK.models import (News, Class, UserProfile)

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['pk',
                  'username',
                  'email',
                  'password', ]

    # def create(self, validated_data):
    #     django_user = User.objects.create_user(username=validated_data.get('username'), password=validated_data.get('password'))
    #     user_profile = UserProfile.ob
    #     return user_profile

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