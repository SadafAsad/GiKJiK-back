"""GiKJiK_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GiKJiK.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth
    path('log-in/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-up/', SignUpView.as_view(), name="sign_up"),

    # user
    path('user/<str:username>/search/', UserRetrieveByUsernameView.as_view(), name="user_search"),
    path('user/<int:user_id>/retrieve/', UserRetrieveByIdView.as_view(), name="user_retrieve"),

    # class
    path('class/create/', ClassCreateView.as_view(), name="class_create"),
    path('class/<str:class_id>/search/', ClassRetrieveView.as_view(), name="class_search"),
    path('class/<str:class_id>/join/', ClassJoinView.as_view(), name="class_join"),
    path('class/<str:class_id>/remove/', ClassRemoveView.as_view(), name="class_remove"),
    path('class/<str:class_id>/delete/', ClassDeleteView.as_view(), name="class_delete"),
    path('class/<str:class_id>/change/status/', ClassChangeStatusView.as_view(), name="class_status_change"),
    path('user/student/in/', UserStudentInClassListView.as_view(), name="user_student_in"),
    path('user/teacher/in/', UserTeacherInClassListView.as_view(), name="user_teacher_in"),
    path('user/owner/of/', UserOwnerOfClassListView.as_view(), name="user_owner_of"),

    # teacher
    path('class/<str:class_id>/teacher/add-remove/', ClassAddRemoveTeacherView.as_view(), name="class_ar_teacher"),

    # student
    path('class/<str:class_id>/student/add-remove/', ClassAddRemoveStudentView.as_view(), name="student_add_remove"),

    # news
    path('class/<str:class_id>/add/news/', NewsCreate.as_view(), name="class_add_news"),
    path('class/<str:class_id>/blackboard/', ClassNewsListView.as_view(), name="class_news"),

    # quiz
    path('class/<str:class_id>/create/quiz/', QuizCreateView.as_view(), name="class_add_quiz"),
    path('quiz/<int:quiz_id>/delete/', QuizDeleteView.as_view(), name="quiz_delete"),
    path('class/<str:class_id>/quiz/list/', ClassQuizListView.as_view(), name="class_quiz_list"),

    # question
    path('quiz/<int:quiz_id>/add/question/', QuestionCreateView.as_view(), name="quiz_add_question"),
    path('quiz/<int:quiz_id>/questions/', QuizQuestionsView.as_view(), name="quiz_questions"),

    # choice
    path('question/<int:question_id>/add/choice/', ChoiceCreateView.as_view(), name="question_add_choice"),
    
    # answer
    path('question/<int:question_id>/create/answer/', CreateAnswerView.as_view(), name="create_answer"),

    # grade
    path('question/<int:question_id>/create/grade/', CreateGradeView.as_view(), name="create_grade"),

    # test
    path('user/list/', UserProfileListView.as_view(), name="user_list"),
    path('class/list/', ClassListView.as_view(), name="class_list"),
    path('test/', Test.as_view(), name="test"),
]
