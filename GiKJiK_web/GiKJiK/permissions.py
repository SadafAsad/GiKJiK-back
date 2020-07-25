from rest_framework import permissions
from django.shortcuts import get_object_or_404
from GiKJiK.models import *

class IsClassOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        if t_class.owner == user.user_profile:
            return True
        return False

class IsClassStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        if t_class.students.filter(django_user=user).exists():
            return True
        return False

class CanCreateNews(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        if t_class.owner == user.user_profile:
            return True
        elif t_class.teachers.filter(django_user=user).exists():
            return True
        else:
            return False

class InClass(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        if t_class.owner == user.user_profile:
            return True
        elif t_class.teachers.filter(django_user=user).exists():
            return True
        elif t_class.students.filter(django_user=user).exists():
            return True
        else:
            return False

class IsClassTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        if t_class.teachers.filter(django_user=user).exists():
            return True
        return False
