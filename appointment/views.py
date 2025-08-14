from django.shortcuts import render
from rest_framework import permissions, viewsets, routers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field='id'

