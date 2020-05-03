#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TotalsSerializer
from core.models import GeneralDataModel

class Totals():

    def __init__(self):
        

        try:
            last = GeneralDataModel.objects.latest('day')
            self.last_update = last.day
            self.infected = last.infecteds
            self.dead = last.deads
            self.lethality = last.lethality
        except GeneralDataModel.DoesNotExist:
            self.last_update = None
            self.infected = None
            self.dead = None
            self.lethality = None

class TotalsView(APIView):
    """
    List totals registers 
    """

    def get(self, request, format=None):
        total = Totals()
        serializer = TotalsSerializer(total)
        return Response(serializer.data)

totals_view = TotalsView.as_view()