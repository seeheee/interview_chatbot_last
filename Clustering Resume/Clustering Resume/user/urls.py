from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    path('create/', views.UserRegistrationView.as_view()),  # 회원가입
    path('login/', views.UserLoginView.as_view()),  # 로그인
    path('logout/', views.UserLogout.as_view()),
]