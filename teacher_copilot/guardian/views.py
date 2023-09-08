from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .forms import GuardianForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Guardian


# Create your views here.
@method_decorator(
    login_required,
    name="dispatch",
)
class CreateGuardianView(View):
    template_name = "guardian/create_guardian.html"
    context = {}
    form_class = GuardianForm

    def get(self, request):
        self.context["form"] = self.form_class

        return render(request, self.template_name, self.context)

    def post(self, request):
        self.form_class = GuardianForm(request.POST)
        self.context["form"] = self.form_class

        if self.form_class.is_valid:
            self.form_class.save()

            return render(request, self.template_name, self.context)
        else:
            return render(request, self.template_name, self.context)


@method_decorator(
    login_required,
    name="dispatch",
)
class ListGuardiansView(View):
    template_name = "guardian/list_guardian.html"
    context = {}

    def get(self, request):
        guardians_list = Guardian.objects.all()
        self.context["guardians_list"] = guardians_list
        if guardians_list:
            print(guardians_list[0])
            return render(request, self.template_name, self.context)
        else:
            self.context[
                "message"
            ] = "Você ainda não tem nenhum  responsável cadastrado..."

            return render(request, self.template_name, self.context)


class DetailGuardiansView(View):
    template_name = "guardian/details_guardian.html"
    context = {"guardian": None}

    def get(self, request, guardian_id):
        guardian_data = Guardian.objects.get(id=guardian_id)
        self.context["guardian"] = guardian_data
        if guardian_data:
            return render(request, self.template_name, self.context)
        else:
            self.context["message"] = "Resposável não encontrado..."

            return render(request, self.template_name, self.context)
