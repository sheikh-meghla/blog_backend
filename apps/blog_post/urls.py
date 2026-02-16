from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostCreateAPIView

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post-list"),
    path("posts/<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateAPIView.as_view(), name="post-create"),
    
]