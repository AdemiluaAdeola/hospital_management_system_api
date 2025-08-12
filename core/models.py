from django.db import models
from user.models import User

# Create your models here.
class Doctor(models.Model):
    
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    bio = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=255, choices=gender_choices)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Dr. " + self.user.first_name + " - " + self.specialty
    
class Laboratory_Scientist(models.Model):
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    bio = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=255, choices=gender_choices)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Lab. Scientist " + self.user.first_name + " - " + self.specialty
    
class Nurse(models.Model):
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    bio = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=255, choices=gender_choices)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Nurse " + self.user.first_name + " - " + self.specialty