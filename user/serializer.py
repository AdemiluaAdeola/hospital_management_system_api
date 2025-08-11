from rest_framework import serializers
from .models import *

#create your seriializers here
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'role',
            'password',
        ]

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
        ]

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = [
            'id',
            'first_name',
            'last_name',
            'role',
        ]

# class PatientCreateSerializer(serializers.ModelSerializer):
#     age = serializers.IntegerField(source='get_age', read_only=True)

#     class Meta:
#         model = Patient
#         fields = [
#             'id',
#             'user',
#             'dob',
#             'gender',
#             'phone',
#             'address',
#             'blood_type',
#             'created_at',
#             'updated_at',
#             'age',  # added as read-only
#         ]
#         read_only_fields = ['created_at', 'updated_at', 'age']