from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.get_username')
    
    created_at = serializers.DateTimeField(format="%d %b, %Y", read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_name', 'created_at', 'updated_at', 'is_published']
        read_only_fields = ['author', 'slug', 'created_at', 'updated_at']

    def validate_title(self, value):
        """টাইটেল খুব ছোট হলে এরর দেবে"""
        if len(value) < 5:
            raise serializers.ValidationError("টাইটেল অন্তত ৫ অক্ষরের হতে হবে।")
        return value