from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/", include("apps.user.urls")),
    path("api/blog/", include("apps.blog_post.urls")),
    path("api/comments/", include("apps.comment.urls")),
    
]
