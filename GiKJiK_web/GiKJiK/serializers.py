from rest_framework import serializers
from GiKJiK.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]
    
    @staticmethod
    def get_username(instance) -> str:
        return instance.username

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password', ]
    
    def validate_password(self, value: str) -> str:
        return make_password(value)

class UserProfileListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['django_user', 'online_in', 'photo', 'username', 'id', ]

    @staticmethod
    def get_username(instance) -> str:
        return instance.django_user.username
    
    @staticmethod
    def get_id(instance) -> int:
        return instance.django_user.id

class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name', 'class_id', ]

class ClassListSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(many=False)
    students = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Class
        fields = '__all__'

class ClassAddRemoveTeacherSerializer(serializers.ModelSerializer):
    ADD = "ADD"
    REMOVE = "REMOVE"

    choices = (ADD,
               REMOVE)

    m_teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    action = serializers.ChoiceField(choices=choices, write_only=True)

    class Meta:
        model = Class
        fields = ['m_teacher', 'action', ]
        extra_kwargs = {
            'teacher': {'read_only': True}
        }

    def validate_m_teacher(self, m_teacher):
        return m_teacher.user_profile

class ClassJoinRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['students', ]
        extra_kwargs = {
            'students': {'read_only': True}
        }

class NewsCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = {
            '_class': {'read_only': True},
            'author': {'read_only': True}
        }

class NewsListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = News
        fields = '__all__'

class ClassAddRemoveStudentSerializer(serializers.ModelSerializer):
    ADD = "ADD"
    REMOVE = "REMOVE"

    choices = (ADD,
               REMOVE)

    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    action = serializers.ChoiceField(choices=choices, write_only=True)

    class Meta:
        model = Class
        fields = ['student', 'action', ]
        extra_kwargs = {
            'students': {'read_only': True}
        }

    def validate_student(self, student):
        return student.user_profile

class QuizeCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)

    class Meta:
        model = Quize
        fields = '__all__'
        extra_kwargs = {
            '_class': {'read_only': True},
            'author': {'read_only': True}
        }

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        extra_kwargs = {
            'quize': {'read_only': True}
        }

class ChoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        extra_kwargs = {
            'question': {'read_only': True}
        }

class ClassChangeStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['state', ]

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['student', 'question', 'answer', ]
        extra_kwargs = {
            'student': {'read_only': True},
            'question': {'read_only': True}
        }

class GradeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        extra_kwargs = {
            'question': {'read_only': True}
        }

class GradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
