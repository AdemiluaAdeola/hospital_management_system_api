from django.db import models
from core.models import *
from patient.models import PatientProfile

# Create your models here.
# class LabTestRequest(models.Model):
#     STATUS_CHOICES = [
#         ("Pending", "Pending"),
#         ("In Progress", "In Progress"),
#         ("Completed", "Completed"),
#         ("Cancelled", "Cancelled"),
#     ]

#     patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="lab_requests")
#     doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="requested_tests")
#     test_name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.test_name} for {self.patient.full_name} - {self.status}"
    
# class LabTestResult(models.Model):
#     attendant = models.ForeignKey(Laboratory_Scientist, on_delete=models.PROTECT, related_name="lab_test_result")
#     request = models.OneToOneField(LabTestRequest, on_delete=models.CASCADE, related_name="lab_result")
#     notes = models.TextField(blank=True, null=True)
#     file = models.FileField(upload_to="lab_results/", blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Result for {self.request.test_name}"

class LabTest(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="lab_requests")
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="requested_tests")
    test_name = models.CharField(max_length=255)
    lab = models.ForeignKey(Laboratory_Scientist, on_delete=models.PROTECT, related_name="lab_test")
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    result = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)