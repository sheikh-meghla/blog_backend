from django.contrib import admin
from .models import Post
from unfold.admin import ModelAdmin

@admin.register(Post)
class PostAdmin(ModelAdmin):
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)