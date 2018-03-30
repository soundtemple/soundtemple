from django.urls import path, re_path
from . import views


urlpatterns = [
    path('add/to_post/<int:pk>', views.AddPostComment.as_view(), name='post_comment_add'),
    path('approve/<int:pk>', views.comment_approve, name='comment_approve'),
    path('remove/<int:pk>', views.comment_remove, name='comment_remove'),
]