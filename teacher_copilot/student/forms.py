from .models import Student
from django.forms import ModelForm
from django import forms


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["created_by", "is_active", "teacher"]
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
