from django.urls import path
from .views import CreateStudentView, ListStudentView, DetailStudentView

app_name = "student"

urlpatterns = [
    path("create", CreateStudentView.as_view(), name="create"),
    path("list", ListStudentView.as_view(), name="list"),
    path("details/<int:id>", DetailStudentView.as_view(), name="details"),
]
