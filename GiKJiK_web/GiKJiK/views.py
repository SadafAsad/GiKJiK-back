from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from GiKJiK.models import *
from GiKJiK.serializers import *
from GiKJiK.permissions import *

class SignUpView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserProfileListView(generics.ListAPIView):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all()

class ClassCreateView(generics.CreateAPIView):
    serializer_class = ClassCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.user_profile)

class ClassListView(generics.ListAPIView):
    serializer_class = ClassListSerializer
    queryset = Class.objects.all()
    
class ClassRetrieveView(generics.RetrieveAPIView):
    serializer_class = ClassListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return get_object_or_404(Class, class_id=self.kwargs.get('class_id'))

class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserProfileListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return user.user_profile

class ClassAddRemoveTeacherView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsClassOwner,)
    queryset = Class.objects.all()
    serializer_class = ClassAddRemoveTeacherSerializer

    lookup_field = 'class_id'
    lookup_url_kwarg = 'class_id'

    def perform_update(self, serializer):
        if serializer.validated_data.get('action') == self.serializer_class.ADD:
            serializer.instance.teachers.add(serializer.validated_data.get('teacher'))
        else:
            serializer.instance.teachers.remove(serializer.validated_data.get('teacher'))
