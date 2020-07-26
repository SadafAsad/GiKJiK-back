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
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-up/', SignUpView.as_view(), name="sign_up"),
    path('user/list/', UserProfileListView.as_view(), name="user_list"),
    path('class/create/', ClassCreateView.as_view(), name="class_create"),
    path('class/list/', ClassListView.as_view(), name="class_list"),
    path('class/<str:class_id>/search/', ClassRetrieveView.as_view(), name="class_search"),
    path('user/<str:username>/search/', UserRetrieveView.as_view(), name="user_search"),
    path('class/<str:class_id>/teacher/add-remove/', ClassAddRemoveTeacherView.as_view(), name="class_ar_teacher"),
    path('class/<str:class_id>/join/', ClassJoinView.as_view(), name="class_join"),
    path('user/class/list/', UserClassListView.as_view(), name="user_class_list"),
    path('class/<str:class_id>/remove/', ClassRemoveView.as_view(), name="class_remove"),
    path('class/<str:class_id>/add/news/', NewsCreate.as_view(), name="class_add_news"),
    path('class/<str:class_id>/blackboard/', ClassNewsListView.as_view(), name="class_newa"),
    path('class/<str:class_id>/student/add-remove/', ClassAddRemoveStudentView.as_view(), name="student_add_remove"),
    path('class/<str:class_id>/create/quiz/', QuizCreateView.as_view(), name="class_add_quiz"),
]
