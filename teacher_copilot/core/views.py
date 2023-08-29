from django.shortcuts import render
from django.views import View
from .forms import LoginForm

# Create your views here.


class IndexTemplateView(View):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        context = {}
        if not request.user.is_authenticated:
            self.template_name = "core/login.html"
            context["forms"] = LoginForm(request.POST or None)
        return render(request, self.template_name, context)
