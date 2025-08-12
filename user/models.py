from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.
class User(AbstractUser):
    gender_choices = (
        ('male', 'male'),
        ('female', 'female'),
    )

    role_choices = (
        ("Admin", "Admin"),
        ("doctor", "doctor"),
        ("Patient", "Patient"),
        ("nurse", "nurse"),
        ("laboratory", "laboratory"),
        ("pharmacy", "pharmacy"),
        ("non-medical", "non-medical"),
    )

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    dob = models.DateField()
    role = models.CharField(max_length=255, choices=role_choices)
    gender = models.CharField(max_length=25, choices=gender_choices)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def get_age(self):
        today = date.today()
        age = today.year - self.dob.year - (
            (today.month, today.day) < (self.dob.month, self.dob.day)
        )
        return age

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    