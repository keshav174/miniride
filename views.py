from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from wakefit.constant import SUCCESS
from .models import DriverDetails, RideDetals
from django.core.serializers import serialize
import json
from django.urls import path

class DriverDetailsAPI(APIView):
    def post(self, request):
        driver_name = request.data['name']
        phn_no = request.data['phone_no']
        print(driver_name,phn_no)
        DriverDetails.objects.create(driver_name=driver_name, phone_no=phn_no)
        return Response({'result': {driver_name, phn_no}, 'status': SUCCESS}, status=status.HTTP_200_OK)


class RideDetailsAPI(APIView):
    def get(self,request,driver_id):
        print(driver_id)
        result = RideDetals.objects.filter(driver_id=driver_id).all()
        data = serialize("json", result,fields=('create_date', 'start_loc','end_loc','amount'))
        return Response({'result': data, 'status': SUCCESS}, status=status.HTTP_200_OK)





