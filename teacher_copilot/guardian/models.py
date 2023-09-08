from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Create your models here.
class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to="guardian_photos", blank=True)
    notes = models.TextField(max_length=500)
    created_by = models.ForeignKey(
        User, related_name="guardians", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
