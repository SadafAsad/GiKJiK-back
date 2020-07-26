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

class CanEditQuiz(permissions.BasePermission):

    def has_permission(self, request, view):
        quiz = get_object_or_404(Quize, pk=view.kwargs.get('quiz_id'))
        user = request.user.user_profile
        return quiz.author == user

class CanEditQuestion(permissions.BasePermission):
    def has_permission(self, request, view):
        question = get_object_or_404(Question, pk=view.kwargs.get('question_id'))
        user = request.user.user_profile
        return question.quize.author == user
