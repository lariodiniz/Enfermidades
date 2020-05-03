#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TotalsSerializer
from core.models import SicksModel

class Totals():

    def __init__(self):
        try:
            self.last_update = SicksModel.objects.latest('infection_identification_date').infection_identification_date
            self.infected = SicksModel.objects.all().count()
            self.dead = SicksModel.objects.filter(person__dead=True,).count() 
            self.lethality = (self.dead * 100) / self.infected
        except SicksModel.DoesNotExist:
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