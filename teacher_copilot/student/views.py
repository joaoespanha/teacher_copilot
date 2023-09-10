from django.shortcuts import render
from django.views import View
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Student


# Create your views here.
@method_decorator(
    login_required,
    name="dispatch",
)
class CreateStudentView(View):
    template_name = "students/student_create.html"
    context = {}
    form_class = StudentForm

    def get(self, request):
        self.context["form"] = self.form_class

        return render(request, self.template_name, self.context)

    def post(self, request):
        self.form_class = StudentForm(request.POST)
        self.context["form"] = self.form_class

        if self.form_class.is_valid():
            new_student = self.form_class.save(commit=False)
            new_student.teacher = request.user
            new_student.save()
            return render(request, self.template_name, self.context)
        else:
            self.context["messsage"] = "ERROR"
            return render(request, self.template_name, self.context)


@method_decorator(
    login_required,
    name="dispatch",
)
class ListStudentView(View):
    template_name = "students/student_list.html"
    context = {}

    def get(self, request):
        students_list = Student.objects.filter(teacher=request.user)
        if students_list:
            self.context["students_list"] = students_list
            return render(request, self.template_name, self.context)
        else:
            self.context[
                "message"
            ] = "Você ainda não tem nenhum  responsável cadastrado..."

            return render(request, self.template_name, self.context)


class DetailStudentView(View):
    template_name = "students/student_details.html"
    context = {}

    def get(self, request, id):
        student = Student.objects.get(id=id)
        if student:
            self.context["student"] = student
            return render(request, self.template_name, self.context)
        else:
            self.context["message"] = "Estudante não encontrado"

            return render(request, self.template_name, self.context)
