from rest_framework import serializers

from GiKJiK.models import (News, Class)
# from cafepay.api_v1.helpers import get_cafe_simple_json, get_cafe_info_serializer, \
#     get_user_profile_basic_info_serializer


def simple_user_profile_json(user_profile):
    return {
        'pk': user_profile.pk,
        'username': user_profile.django_user.username,
        'full_name': user_profile.full_name
    }

class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['pk', 'name', 'class_id', 'owner', ]
        extra_kwargs = {'owner': {'read_only': True}}

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['pk', '_classes', 'title', 'description', 'date']

# sign up kardan --> username, email, password