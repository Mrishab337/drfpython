from django.shortcuts import render
from rest_framework import viewsets
from .models import Businessregister
from .serializers import BusinessregisterSerializer

# Create your views here.

class BusinessregisterViewSet(viewsets.ModelViewSet):
    queryset = Businessregister.objects.all()
    serializer_class = BusinessregisterSerializer