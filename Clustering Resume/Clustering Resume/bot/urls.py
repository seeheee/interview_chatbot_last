from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('cam', views.chatbot_cam, name='chatbot_cam'),
    path('bot', views.bot, name='bot'),
    path('stopwatch', views.stopwatch, name='bot'),
    path('button_real', views.button_real, name='bot'),
    path('gan', views.gan, name='bot'),
    path('logo', views.logo, name='bot'),
    path('mirime', views.mirime, name='bot'),
    path('bottom', views.bottom, name='bot'),
    path('soundwave', views.soundwave, name='bot'),
    path('/home/mypage/', views.mypage, name="mypage"),
]