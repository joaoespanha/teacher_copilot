from django.urls import path
from .views import DashBoardView


app_name = "core"

urlpatterns = [
    path("", DashBoardView.as_view(), name="dashboard"),
]
