from django.db import models
from django.contrib.auth.models import User
from GiKJiK.consts import (QuizConsts, AnswerConsts, ClassConsts)

# Create your models here.
class UserProfile(models.Model):

    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    online_in = models.ForeignKey("Class", on_delete=models.CASCADE, related_name="online_users", null=True)

    # username = models.CharField(max_length=225, unique=True)
    # password = models.CharField(max_length=225, blank=False, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    photo = models.ImageField(max_length=225, blank=True)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

class Class(models.Model):

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="owner_classes")
    teacher = models.ManyToManyField(UserProfile, related_name="teacher_classes", blank=True)
    student = models.ManyToManyField(UserProfile, related_name="member_classes", blank=True)

    name = models.CharField(max_length=225, blank=False)
    class_id = models.CharField(max_length=225, unique=True, blank=False, null=False)
    state = models.CharField(max_length=225, choices=ClassConsts.states, default=ClassConsts.OFFLINE)

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
    q_type = models.CharField(max_length=225, choices=QuizConsts.types)
    deadline = models.DateTimeField(auto_now=False)
    state = models.CharField(max_length=225, choices=QuizConsts.states)

class Question(models.Model):

    quize = models.ForeignKey(Quize, on_delete=models.CASCADE, related_name="questions")

    problem = models.CharField(max_length=225, blank=False)
    solution = models.CharField(max_length=225, blank=True)
    point = models.IntegerField()

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    description = models.CharField(max_length=225, )

class Grade(models.Model):

    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="std_grades")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_grades")

    grade = models.IntegerField()

class Answer(models.Model):

    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="std_answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answers")

    answer = models.CharField(max_length=225, blank=True)
    ans_type = models.CharField(max_length=225, choices=AnswerConsts.types)
    ans_state = models.CharField(max_length=225, choices=AnswerConsts.states, default=AnswerConsts.NOT_ANSWERED)
