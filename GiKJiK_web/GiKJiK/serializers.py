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

class ClassAddRemoveTeacherSerializer(serializers.ModelSerializer):
    ADD = "ADD"
    REMOVE = "REMOVE"

    choices = (ADD,
               REMOVE)

    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    action = serializers.ChoiceField(choices=choices, write_only=True)

    class Meta:
        model = Class
        fields = ['teacher', 'action', ]
        extra_kwargs = {
            'teachers': {'read_only': True}
        }

    def validate_teacher(self, teacher):
        return teacher.user_profile

class ClassJoinRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['students', ]
        extra_kwargs = {
            'students': {'read_only': True}
        }
