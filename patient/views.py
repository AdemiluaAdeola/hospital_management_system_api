from django.shortcuts import render
from rest_framework import status, permissions, generics, viewsets, routers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PatientProfile
from .serializer import PatientSerializer, PatientListSerializer

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')