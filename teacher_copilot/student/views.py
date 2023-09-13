from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Student
from .utils import DatesHandler


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
        teacher = request.user

        if self.form_class.is_valid():
            updaated_student = self.form_class.save(commit=False)
            updaated_student.save()
            updaated_student.teacher.set([teacher])
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
        teacher = request.user

        self.context["teacher"] = teacher

        students_list = Student.objects.filter(teacher=teacher)

        self.context = {}

        if students_list:
            self.context["students_list"] = students_list
            return render(request, self.template_name, self.context)
        else:
            self.context[
                "message"
            ] = "Você ainda não tem nenhum  responsável cadastrado..."

            return render(request, self.template_name, self.context)


@method_decorator(
    login_required,
    name="dispatch",
)
class DetailStudentView(View):
    template_name = "students/student_details.html"
    context = {}

    def get(self, request, id):
        student = Student.objects.get(id=id)
        if student:
            self.context["student"] = student
            self.context["age"] = DatesHandler.calculate_age(student.birthday)

            return render(request, self.template_name, self.context)
        else:
            self.context["message"] = "Estudante não encontrado"

            return render(request, self.template_name, self.context)


class DeleteStudentView(View):
    template_name = "students/student_details.html"
    context = {}

    def get(self, request, id):
        student = get_object_or_404(Student, id=id)

        teacher = student.teacher.filter(id=request.user.id)
        if teacher:
            student.delete()
            return redirect("student:list")
        else:
            return render(request, self.template_name, self.context)


class EditStudentView(View):
    template_name = "students/student_create.html"
    context = {}
    form_class = StudentForm
    model = Student

    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        teacher = student.teacher.filter(id=request.user.id)
        self.context["title"] = "Edit"
        if teacher:
            self.context["form"] = self.form_class(instance=student)
        else:
            self.context["message"] = "Esse estudante não é seu para editar"

        return render(request, self.template_name, self.context)

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)

        self.form_class = StudentForm(request.POST, instance=student)
        self.context["form"] = self.form_class

        if self.form_class.is_valid():
            student.save()

            return redirect("student:details", id=id)
        else:
            self.context["messsage"] = "ERROR"
            return render(request, self.template_name, self.context)
