from django.db import models
from user.models import User

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=2000000000000000000000000000000000000000000000000)
    code = models.CharField(max_length=50)
    location = models.TextField()
    bio = models.TextField()
    logo = models.URLField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
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
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
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
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
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