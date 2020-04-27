from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateUpdateView, ArticleDeleteView
from . import views

urlpatterns = [
    path('', ArticleListView.as_view()),  # 리스트
    path('create/', ArticleCreateUpdateView.as_view()),  # 게시물 작성
    path('<article_id>/', ArticleDetailView.as_view()),  # 상세페이지
    path('<article_id>/update/', ArticleCreateUpdateView.as_view()),  # 게시물 업데이트
    path('<article_id>/delete/', ArticleDeleteView.as_view()),
]