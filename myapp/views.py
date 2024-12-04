from django.shortcuts import render
from rest_framework import viewsets
from .models import Businessregister
from .serializers import BusinessregisterSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# Create your views here.

class BusinessregisterViewSet(viewsets.ModelViewSet):
    queryset = Businessregister.objects.all()
    serializer_class = BusinessregisterSerializer
    
    
    
    ###- for name suggetions [ not used ] ##
    
# @api_view(['GET'])
# def namesuggetions(request):
#     suggetions=[]
#     business = Businessregister.objects.all()
#     existednames=[business.workspacename for business in business]
#     basename=request.query_params.get('basename','workspace')
#     for i in range(1,6):
#         suggetions=f"{basename}_{i}"
#         if suggetions not in existednames:
#             suggetions.append(suggetions)
#         return Response(suggetions)
    
    
