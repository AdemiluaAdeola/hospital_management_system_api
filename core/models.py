from django.db import models
from user.models import User

# Create your models here.
class StaffBase(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    bio = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Doctor(StaffBase):
    def __str__(self):
        return f"Dr. {self.user.first_name} - {self.specialty}"


class Laboratory_Scientist(StaffBase):
    def __str__(self):
        return f"Lab. Scientist {self.user.first_name} - {self.specialty}"


class Nurse(StaffBase):
    def __str__(self):
        return f"Nurse {self.user.first_name} - {self.specialty}"
