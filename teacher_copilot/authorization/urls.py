from django.urls import path
from .views import AuthenticationTemplateView, SignUpView, LogoutView


app_name = "authorization"

urlpatterns = [
    path("login", AuthenticationTemplateView.as_view(), name="login"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("logout", LogoutView.as_view(), name="logout"),
]
