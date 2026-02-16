from django.urls import path
from .views import CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path("comments/<int:post_id>/", CommentListCreateAPIView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    
]