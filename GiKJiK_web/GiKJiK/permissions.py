from rest_framework import permissions
from django.shortcuts import get_object_or_404
from GiKJiK.models import *

class IsClassOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        return t_class.owner == user.user_profile

class IsClassStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        return t_class.students.filter(django_user=user).exists()

class CanCreateNews(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        return (t_class.owner == user.user_profile) or (t_class.teachers.filter(django_user=user).exists())

class InClass(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        return (t_class.owner == user.user_profile) or (t_class.teachers.filter(django_user=user).exists()) or (t_class.students.filter(django_user=user).exists())

class IsClassTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        return t_class.teachers.filter(django_user=user).exists()

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

class IsClassTeacher_or_Student_by_quiz(permissions.BasePermission):

    def has_permission(self, request, view):
        quiz = get_object_or_404(Quize, pk=view.kwargs.get('quiz_id'))
        user = request.user
        return (quiz.author == user.user_profile) or (quiz._class.students.filter(django_user=user).exists())
        
class IsClassStudent_by_question(permissions.BasePermission):

    def has_permission(self, request, view):
        question = get_object_or_404(Question, pk=view.kwargs.get('question_id'))
        user = request.user
        return question.quize._class.students.filter(django_user=user).exists()

class IsQuizauthor_by_question(permissions.BasePermission):

    def has_permission(self, request, view):
        question = get_object_or_404(Question, pk=view.kwargs.get('question_id'))
        user = request.user.user_profile
        return question.quize.author == user
