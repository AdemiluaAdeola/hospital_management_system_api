from rest_framework import serializers
from .models import Appointment
from patient.serializer import *

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientListSerializer()
    class Meta:
        model = Appointment
        fields = '__all__'