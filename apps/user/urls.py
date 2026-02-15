from django.urls import path, include

urlpatterns = [
    path("signup/", include("apps.user.signup_urls")),
    path("signin/", include("apps.user.signin_urls")),
    path("signout/", include("apps.user.signout_urls")),
    path("profile/", include("apps.user.profile_urls")),
    path("change-password/", include("apps.user.change_password_urls")),
]