from django.db import settings
from django.db import models

class Comment(models.Model):    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="user_comments"
    )
    
    # কমেন্টের লেখা
    content = models.TextField(max_length=500)
    
    # রিপ্লাই সিস্টেমের জন্য
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
        return f"Comment by {self.user.username} - {self.content[:20]}"

    @property
    def is_reply(self):
        return self.parent is not None