from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('list/<tag>/', views.TaggedArticleListView.as_view(), name='tagged-article-list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('edit/<int:pk>/', views.ArticleUpdateView.as_view(), name='article-edit'),
    path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('comment_approve/<int:pk>', views.comment_approve, name='comment_approve'),
]
