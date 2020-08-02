from rest_framework import permissions
from django.shortcuts import get_object_or_404
from GiKJiK.models import *

class IsClassOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        return t_class.owner == request.user.user_profile

class IsClassStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        return t_class.students.filter(django_user=request.user).exists()

class CanCreateNews(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        return (t_class.owner == request.user.user_profile) or (t_class.teacher == request.user.user_profile)

class InClass(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        return (t_class.owner == request.user.user_profile) or (t_class.teacher == request.user.user_profile) or (t_class.students.filter(django_user=request.user).exists())

class IsClassTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        return t_class.teacher == request.user.user_profile

class CanEditQuiz(permissions.BasePermission):

    def has_permission(self, request, view):
        quiz = get_object_or_404(Quize, pk=view.kwargs.get('quiz_id'))
        return quiz.author == request.user.user_profile

class CanEditQuestion(permissions.BasePermission):

    def has_permission(self, request, view):
        question = get_object_or_404(Question, pk=view.kwargs.get('question_id'))
        return question.quize.author == request.user.user_profile

class IsClassTeacher_or_Student_by_quiz(permissions.BasePermission):

    def has_permission(self, request, view):
        quiz = get_object_or_404(Quize, pk=view.kwargs.get('quiz_id'))
        return (quiz.author == request.user.user_profile) or (quiz._class.students.filter(django_user=request.user).exists())
        
class IsClassStudent_by_question(permissions.BasePermission):

    def has_permission(self, request, view):
        question = get_object_or_404(Question, pk=view.kwargs.get('question_id'))
        return question.quize._class.students.filter(django_user=request.user).exists()

class IsQuizauthor_by_question(permissions.BasePermission):

    def has_permission(self, request, view):
        question = get_object_or_404(Question, pk=view.kwargs.get('question_id'))
        return question.quize.author == request.user.user_profile

class IsNewsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        news = get_object_or_404(News, pk=view.kwargs.get('news_id'))
        return news.author == request.user.user_profile
