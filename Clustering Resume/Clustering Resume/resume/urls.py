from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path('new/', views.resume_new, name='resume_new'),
    path('<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('mbti_test/', views.mbti_test, name='mbti_test'),
    path('update_pro/', views.update_pro, name='update_pro'),
]