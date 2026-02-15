from tokenize import Comment
from django.contrib import admin

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("user__username", "content")
    ordering = ("-created_at",)
    fieldsets = (
        (None, {"fields": ("user", "content", "parent")}),
        ("Status", {"fields": ("is_active",)}),
    )