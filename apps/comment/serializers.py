from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user_name', 'content', 'parent', 'replies', 'created_at']
        read_only_fields = ['created_at']

    def get_replies(self, obj):
        if obj.parent is None:
            return CommentSerializer(obj.replies.all(), many=True).data
        return None