from django.conf.urls import url
from django.urls import path
from . import views
from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('new/', ArticleCreateView.as_view(), name='article-create'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article-edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),


    # url(r'^test$', views.test, name='test'),
    # path(r'list', views.BlogPageView.as_view(), name='blog_list'),
]
