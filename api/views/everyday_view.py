#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import EverydaySerializer
from core.models import GeneralDataModel

class EverydayView(APIView):
    """
    List day registers 
    """

    def get(self, request, format=None):
        objects = GeneralDataModel.objects.all()
        serializer = EverydaySerializer(objects, many=True)
        return Response(serializer.data)


everyday_view = EverydayView.as_view()