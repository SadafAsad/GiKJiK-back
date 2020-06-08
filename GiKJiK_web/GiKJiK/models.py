from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    django_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=225, unique=True)
    email = models.EmailField(max_length=255, blank=False, null=False, primary_key=True)
    password = models.CharField(max_length=225)

class Class(models.Model):

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="owner_classes")
    teacher = models.ManyToManyField(UserProfile, related_name="teacher_classes", blank=True)
    member = models.ManyToManyField(UserProfile, related_name="member_classes", blank=True)

    name = models.CharField(max_length=225)
    class_id = models.CharField(max_length=225, primary_key=True, blank=False, null=False)

class News(models.Model):

    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="news")

    title = models.CharField(max_length=225, blank=False)
    description = models.TextField(blank=True)

class WhiteBoard(models.Model):

    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="white_boards")

class Chatroom(models.Model):

    _class = models.OneToOneField(Class, on_delete=models.CASCADE, related_name="chat_room")

class Quize(models.Model):

    _class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="class_quizes")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="author_quizes")

class Question(models.Model):

    quize = models.ForeignKey(Quize, on_delete=models.CASCADE, related_name="questions")

    problem = models.CharField(blank=False)
    grade = models.IntegerField()

class Grade(models.Model):

    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="std_grades")
    question = models.Model(Question, on_delete=models.CASCADE, related_name="question_grades")
