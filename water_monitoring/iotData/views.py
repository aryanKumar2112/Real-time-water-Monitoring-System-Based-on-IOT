from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from iotData.serializers import IotDataSerializer

from .models import IotData

class iotDataView(APIView):
    def get(self, request):
        data = IotData.objects.all()
        print(data)
        serializer = IotDataSerializer(data, many=True)
        print(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        
        iotData = IotData.objects.create(temperature=data.get('temperature'), pHValue=data.get('pHValue'), turbidity=data.get('turbidity'))
        iotData.save()
        
        return Response(data, status=status.HTTP_200_OK)