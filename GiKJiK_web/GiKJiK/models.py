from django.db import models
from django.contrib.auth.models import User
from GiKJiK.consts import (QuizConsts, AnswerConsts, ClassConsts)

# Create your models here.
class UserProfile(models.Model):

    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False, null=False, primary_key=True)
    photo = models.ImageField(max_length=225, blank=True)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

class Class(models.Model):

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="owner_classes")
    teacher = models.ManyToManyField(UserProfile, related_name="teacher_classes", blank=True)
    student = models.ManyToManyField(UserProfile, related_name="member_classes", blank=True)

    name = models.CharField(max_length=225, blank=False)
    class_id = models.CharField(max_length=225, primary_key=True, blank=False, null=False)
    state = models.CharField(choices=ClassConsts.states, default=ClassConsts.OFFLINE)

class News(models.Model):

    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="news")

    title = models.CharField(max_length=225, blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)

class WhiteBoard(models.Model):

    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="white_boards")

class Chatroom(models.Model):

    _class = models.OneToOneField(Class, on_delete=models.CASCADE, related_name="chat_room")

class Quize(models.Model):

    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="class_quizes")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="author_quizes")

    date = models.DateTimeField(auto_now=True)
    q_type = models.CharField(choices=QuizConsts.types)

class Question(models.Model):

    quize = models.ForeignKey(Quize, on_delete=models.CASCADE, related_name="questions")

    problem = models.CharField(blank=False)
    point = models.IntegerField()
    choice_1 = models.CharField(blank=True)
    choice_2 = models.CharField(blank=True)
    choice_3 = models.CharField(blank=True)
    choice_4 = models.CharField(blank=True)

class Grade(models.Model):

    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="std_grades")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_grades")

    grade = models.IntegerField()

class Answer(models.Model):

    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="std_answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answers")

    answer = models.TextField(blank=True)
    ans_type = models.CharField(choices=AnswerConsts.types)
    ans_state = models.CharField(choices=AnswerConsts.states, default=AnswerConsts.NOT_ANSWERED)
    # soale testi
