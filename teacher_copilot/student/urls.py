from django.urls import path
from .views import (
    CreateStudentView,
    ListStudentView,
    DetailStudentView,
    DeleteStudentView,
    EditStudentView,
)

app_name = "student"

urlpatterns = [
    path("create", CreateStudentView.as_view(), name="create"),
    path("list", ListStudentView.as_view(), name="list"),
    path("details/<int:id>", DetailStudentView.as_view(), name="details"),
    path("delete/<int:id>", DeleteStudentView.as_view(), name="delete"),
    path("edit/<int:id>", EditStudentView.as_view(), name="edit"),
]
