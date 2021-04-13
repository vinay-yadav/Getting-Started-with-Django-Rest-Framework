from django.urls import path
from .views import PostList, VoteCreate, DeletePost

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),
    path('posts/<int:pk>/vote/', VoteCreate.as_view(), name='up_vote'),
]
