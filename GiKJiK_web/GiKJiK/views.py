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

class ClassJoinView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Class.objects.all()
    serializer_class = ClassJoinRemoveSerializer

    lookup_field = 'class_id'
    lookup_url_kwarg = 'class_id'

    def perform_update(self, serializer):
        serializer.instance.students.add(self.request.user.user_profile)

class UserClassListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassListSerializer

    def get_queryset(self):
        user = self.request.user.user_profile
        return user.member_classes.all()

class ClassRemoveView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsClassStudent, )
    queryset = Class.objects.all()
    serializer_class = ClassJoinRemoveSerializer

    lookup_field = 'class_id'
    lookup_url_kwarg = 'class_id'

    def perform_update(self, serializer):
        serializer.instance.students.remove(self.request.user.user_profile)

class NewsCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, CanCreateNews, )
    serializer_class = NewsCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.user_profile, _class=get_object_or_404(Class, class_id=self.kwargs.get('class_id')))

class ClassNewsListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, InClass, )
    serializer_class = NewsListSerializer

    def get_queryset(self):
        t_class = get_object_or_404(Class, class_id=self.kwargs.get('class_id'))
        return t_class.news.all()

class ClassAddRemoveStudentView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsClassTeacher,)
    queryset = Class.objects.all()
    serializer_class = ClassAddRemoveStudentSerializer

    lookup_field = 'class_id'
    lookup_url_kwarg = 'class_id'

    def perform_update(self, serializer):
        if serializer.validated_data.get('action') == self.serializer_class.ADD:
            serializer.instance.students.add(serializer.validated_data.get('student'))
        else:
            serializer.instance.students.remove(serializer.validated_data.get('student'))

class QuizCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsClassTeacher, )
    queryset = Class.objects.all()
    serializer_class = QuizeCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.user_profile, _class=get_object_or_404(Class, class_id=self.kwargs.get('class_id')))

class QuestionCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, CanEditQuiz, )
    queryset = Quize.objects.all()
    serializer_class = QuestionCreateSerializer

    def perform_create(self, serializer):
        serializer.save(quize=get_object_or_404(Quize, pk=self.kwargs.get('quiz_id')))

class ChoiceCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, CanEditQuestion, )
    queryset = Question.objects.all()
    serializer_class = ChoiceCreateSerializer

    def perform_create(self, serializer):
        serializer.save(question=get_object_or_404(Question, pk=self.kwargs.get('question_id')))

class QuizDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, CanEditQuiz, )
    queryset = Quize.objects.all()
    serializer_class = QuizeCreateSerializer

    lookup_field = 'pk'
    lookup_url_kwarg = 'quiz_id'

class ClassDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsClassOwner, )
    queryset = Class.objects.all()
    serializer_class = ClassListSerializer

    lookup_field = 'class_id'
    lookup_url_kwarg = 'class_id'

class ClassChangeStateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsClassTeacher, )
    queryset = Class.objects.all()
    serializer_class = ClassChangeStateSerializer

    lookup_field = 'class_id'
    lookup_url_kwarg = 'class_id'

    def perform_update(self, serializer):
        serializer.instance.state = serializer.validated_data.get('state')
        serializer.save()

class ClassQuizListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, InClass, )
    serializer_class = QuizeCreateSerializer

    def get_queryset(self):
        t_class = get_object_or_404(Class, class_id=self.kwargs.get('class_id'))
        return t_class.class_quizes.all()
