from rest_framework import serializers
from .models import Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CommentSerializer(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    replies = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
            'replies',
        ]

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment cannot be empty.")
        return value
