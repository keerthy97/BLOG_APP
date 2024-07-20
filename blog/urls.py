from django.urls import path
from .views import PostList, like_post, PostListCreate, PostRetrieveUpdateDestroy, CommentListCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:post_id>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
