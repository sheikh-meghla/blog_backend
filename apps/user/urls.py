from django.urls import path
from .views import SignUpAPIView, SignInAPIView, SignOutAPIView, ChangePasswordAPIView

urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="signup"),
    path("signin/", SignInAPIView.as_view(), name="signin"),
    path("signout/", SignOutAPIView.as_view(), name="signout"),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change-password"),
]