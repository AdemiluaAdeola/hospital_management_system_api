from django.shortcuts import render
from rest_framework import permissions, viewsets, routers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *

# Create your views here.
class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'