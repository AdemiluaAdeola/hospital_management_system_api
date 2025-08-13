from core.models import *
from rest_framework import serializers
from user.serializer import UserListSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    class Meta:
        model = Nurse
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    class Meta:
        model = Laboratory_Scientist
        fields = '__all__'