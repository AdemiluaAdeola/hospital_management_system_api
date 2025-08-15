from core.models import *
from rest_framework import serializers
from user.serializer import UserListSerializer

class StaffBaseSerializer(serializers.ModelSerializer):
    user = UserListSerializer()  # Or use a nested serializer if you want detailed user info

    class Meta:
        model = Doctor  # This is just a placeholder; subclasses will override it
        fields = [
            "id",
            "user",
            "specialty",
            "level",
            "license",
            "bio",
            "dob",
            "gender",
            "phone",
            "address",
            "created_at",
            "updated_at",
        ]


class DoctorSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Doctor

class LaboratoryScientistSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Laboratory_Scientist


class NurseSerializer(StaffBaseSerializer):
    class Meta(StaffBaseSerializer.Meta):
        model = Nurse