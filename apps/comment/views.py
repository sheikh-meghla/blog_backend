from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from .models import Comment
from .serializers import CommentSerializer
from apps.blog_post.models import Post

class CommentListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, post_id):
        comments = Comment.objects.filter(
            post_id=post_id,
            parent__isnull=True,
            is_active=True
        )
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user,
                post=post
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)

        # Only comment owner can update
        if comment.user != request.user:
            return Response(
                {"error": "You do not have permission to edit this comment."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)

        # Only owner can delete
        if comment.user != request.user:
            return Response(
                {"error": "You do not have permission to delete this comment."},
                status=status.HTTP_403_FORBIDDEN
            )

        comment.delete()
        return Response(
            {"message": "Comment deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )