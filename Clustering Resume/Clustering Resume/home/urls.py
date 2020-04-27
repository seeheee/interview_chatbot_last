from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('details/', views.details, name="details"),
   # path('details-basic/', views.detailsBasic, name="courseDetailsBasic"),
   #  path('list/', views.list, name="list"),
   #  path('listlist/', views.listlist, name="list"),
    path('mypage/', views.mypage, name="mypage"),
    path('result_list/', views.result_list, name="result_list"),
    # path('result_list/<resumes.id>', views.result_details, name="result_details"),
    # path('result_details/<resumes.id>/listlist', views.listlist, name="listlist"),
]
