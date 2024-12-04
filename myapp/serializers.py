from rest_framework import serializers
from .models import Businessregister


class BusinessregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businessregister
        fields = '__all__'
        
    def validated_workspacename(self, value):
        if Businessregister.objects.filter(workspacename=value).exists():
            raise serializers.ValidationError("already exists")
        return value
    def create(self, validated_data):
        return Businessregister.objects.create(**validated_data)
