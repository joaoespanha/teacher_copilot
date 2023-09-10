from .models import Guardian
from django.forms import ModelForm


class GuardianForm(ModelForm):
    class Meta:
        model = Guardian
        fields = "__all__"
        exclude = ["created_by"]
