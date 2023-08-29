from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from guardian.models import Guardian


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    guardians = models.ManyToManyField(
        Guardian,
        related_name="students",
    )
    teacher = models.ManyToManyField(User)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    favorite_subject = models.CharField(max_length=50)
    grade = models.CharField(max_length=20)
    notes = models.TextField(max_length=500)
    birthday = models.DateField()
    football_team = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="student_photos", blank=True)
    instagram = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
