from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import CustomUser

@admin.register(CustomUser)

class CustomUserAdmin(ModelAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Groups and Permissions", {"fields": ("groups", "user_permissions")}),
    )
    search_fields = ("email",)


