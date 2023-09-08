from django.urls import path
from .views import CreateGuardianView, ListGuardiansView, DetailGuardiansView


app_name = "guardian"

urlpatterns = [
    path("create", CreateGuardianView.as_view(), name="create"),
    path("", ListGuardiansView.as_view(), name="list"),
    path("details/<int:guardian_id>", DetailGuardiansView.as_view(), name="details"),
]
