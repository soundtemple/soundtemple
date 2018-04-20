from django.urls import path, re_path
from . import views


urlpatterns = [
    path('add/', views.AddComment.as_view(), name='comment_add'),
    path('approve/<int:pk>', views.comment_approve, name='comment_approve'),
    path('delete/<int:pk>', views.CommentDelete.as_view(), name='comment_delete'),
    path('feature/<int:pk>/<str:feature>', views.comment_feature_toggle, name='comment_feature_toggle'),
    path('list', views.CommentsListView.as_view(), name='comment-list'),
    path('testimonials/', views.TestimonialList.as_view(), name='testimonial-list'),
]
