from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required, name="dispatch")
class DashBoardView(TemplateView):
    template_name = "core/dashboard.html"
