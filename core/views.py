from django.shortcuts import render
from rest_framework import permissions, viewsets, routers
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import *
from core.serializer import *
from appointment.views import AppointmentViewSet
from lab.views import LabTestViewSet
from patient.views import PatientViewSet

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

class LabViewSet(viewsets.ModelViewSet):
    queryset = Laboratory_Scientist.objects.all()
    serializer_class = LaboratoryScientistSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet, basename='doctor')
router.register(r'nurse', NurseViewSet, basename='nurse')
router.register(r'lab', LabViewSet, basename='lab')
router.register(r'appointment', AppointmentViewSet, basename='appointment')
router.register(r'test', LabTestViewSet, basename='test')
router.register(r'patients', PatientViewSet, basename='patient')