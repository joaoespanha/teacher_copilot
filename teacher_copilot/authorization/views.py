from django.shortcuts import render, redirect
from .forms import LoginForm, SingUpForm
from django.views import View
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class AuthenticationTemplateView(View):
    template_name = "authorization/login.html"
    form_class = LoginForm
    context = {}

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.form_class = LoginForm(request.POST)
        self.context = {"form": self.form_class}

        if self.form_class.is_valid:
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:dashboard")
        else:
            return render(request, self.template_name, self.context)


class SignUpView(View):
    template_name = "authorization/signup.html"
    form_class = SingUpForm

    def get(self, request, *args, **kwargs):
        context = {"form": self.form_class}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.form_class = SingUpForm(request.POST)
        if self.form_class.is_valid():
            self.form_class.save()
            return redirect("authorization:login")

        return render(request, "authorization/signup.html", {"form": self.form_class})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("authorization:login")
