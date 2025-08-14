from rest_framework import serializers
from .models import LabTest
from core.models import *
from patient.serializer import PatientListSerializer
from patient.models import PatientProfile


class LabTestSerializer(serializers.ModelSerializer):
    patient = PatientListSerializer()

    class Meta:
        model=LabTest
        fields = '__all__'