from django.db import models
from core.models import Doctor
from patient.models import PatientProfile

# Create your models here.
class Appointment(models.Model):
    status_choices = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("cancelled", "cancelled"),
    )

    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True, related_name="patient_appointments")
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField()