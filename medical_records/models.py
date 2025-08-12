from django.db import models
from patient.models import PatientProfile
from core.models import Doctor
from appointment.models import Appointment

# Create your models here.
class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="medical_record")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, related_name="patient_record")
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL)
    visit_date = models.DateTimeField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    treatment_plan = models.TextField()

class Prescription(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name="prescription")
    drug_name = models.CharField(max_length=200000000000000)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    note = models.TextField()