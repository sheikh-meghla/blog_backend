from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny] 

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug' 

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser] 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)