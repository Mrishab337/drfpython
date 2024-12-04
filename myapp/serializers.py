from rest_framework import serializers
from .models import Businessregister


class BusinessregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessregister
        fields = '__all__'