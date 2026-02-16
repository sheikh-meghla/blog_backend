from django.urls import path
from .views import CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path("comments/<int:post_id>/", CommentListCreateAPIView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    
]
# only one comment list ar url "http://127.0.0.1:8000/api/comments/comments/1/"
# comment detail ar url "http://127.0.0.1:8000/api/comments/comments/123/"
# comment create ar url "http://127.0.0.1:8000/api/comments/comments/1/"

