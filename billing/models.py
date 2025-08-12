from django.db import models
from user.models import User
from patient.models import PatientProfile

# Create your models here.
class Invoice(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Cancelled", "Cancelled"),
    ]

    patient = models.ForeignKey(PatientProfile, on_delete=models.PROTECT, related_name="invoices")
    issued_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="issued_invoices")
    date_issued = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def update_total(self):
        total = self.items.aggregate(total=models.Sum("line_total"))["total"] or 0
        self.total_amount = total
        self.save()

    def __str__(self):
        return f"Invoice #{self.id} for {self.patient.full_name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=255)  # e.g., "Blood Test", "X-Ray"
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        self.invoice.update_total()

    def __str__(self):
        return f"{self.description} x {self.quantity}"
