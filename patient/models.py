from django.db import models
from core.models import Hospital
from datetime import date

# Create your models here.
class PatientProfile(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="patients")
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    blood_type_choices = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )

    full_name = models.CharField(max_length=200000000)
    dob = models.DateField()
    gender = models.CharField(max_length=255, choices=gender_choices)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    blood_type = models.CharField(max_length=255, choices=blood_type_choices)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    #emergency contact
    contact_relationship_choices = (
        ("father", "father"),
        ("mother", "mother"),
        ("brother", "brother"),
        ("sister", "sister"),
        ("cousin", "cousin"),
        ("guardian", "guardian"),
        ("uncle", "uncle"),
        ("aunt", "aunt"),
    )

    contact_name = models.CharField(max_length=2000000000)
    contact_relation = models.CharField(max_length=255, choices=contact_relationship_choices)
    contact_phone=models.PositiveBigIntegerField()

    @property
    def get_age(self):
        today = date.today()
        age = today.year - self.dob.year - (
            (today.month, today.day) < (self.dob.month, self.dob.day)
        )
        return age

    def __str__(self):
        return self.full_name