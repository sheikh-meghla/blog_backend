from django.db import models
from django.conf import settings 
from apps.blog_post.models import Post 

class Comment(models.Model):    
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Post"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="user_comments"
    )
    
    content = models.TextField(max_length=500)
    
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name="replies"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        user_id = self.user.get_username() if self.user else "Unknown"
        post_title = self.post.title if self.post else "No Post"
        return f"Comment by {user_id} on {post_title}"

    @property
    def is_reply(self):
        return self.parent is not None
