from rest_framework import serializers
from patient.models import PatientProfile

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(source='get_age', read_only=True)

    class Meta:
        model = PatientProfile
        fields = [
            'id',
            'full_name',
            'gender',
            'phone',
            'address',
            'blood_type',
            'created_at',
            'updated_at',
            'age',
            'contact_name',
            'contact_relation',
            'contact_phone',
        ]
        read_only_fields = ['created_at', 'updated_at', 'age']

class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientProfile
        fields = [
            'id',
            'full_name',
            'gender',
        ]