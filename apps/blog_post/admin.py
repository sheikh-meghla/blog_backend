from django.contrib import admin
from .models import Post
from unfold.admin import ModelAdmin

@admin.register(Post)
class PostAdmin(ModelAdmin):

    list_display = ("title", "author","is_published")
    prepopulated_fields = {"slug": ("title",)}    
