from django.contrib import admin
from .models import Comment
from unfold.admin import ModelAdmin

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ("user", "content", "short_post_title", "created_at", "is_active")

    @admin.display(description='Post Title') 
    def short_post_title(self, obj):
        if obj.post and obj.post.title:
            return obj.post.title[:20] + "..." if len(obj.post.title) > 20 else obj.post.title
        return "No Post"
    
    