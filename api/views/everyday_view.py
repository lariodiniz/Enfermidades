#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import EverydaySerializer
from core.models import SicksModel

class RegisterDay():

    def __init__(self, day, infected_old, dead_old):
        brazil_population = 211462943
        self.id = 0
        self.day = day
        self.infected = SicksModel.objects.filter(infection_identification_date__lte=day).count()
        self.infected_porcents = (self.infected * 100) / brazil_population
        self.infected_news = self.infected - infected_old
        
        try:
            self.infected_news_porcents = (self.infected_news* 100) / self.infected
        except ZeroDivisionError:
            self.infected_news_porcents = 0

        self.dead = SicksModel.objects.filter(infection_identification_date__lte=day
        ,person__dead=True).count()

        self.dead_porcents = (self.dead * 100) / brazil_population
        self.dead_news = self.dead - dead_old

        try:
            self.dead_news_porcents = (self.dead_news* 100) / self.dead
        except ZeroDivisionError:
            self.dead_news_porcents = 0

        try:
            self.lethality = (self.dead * 100) / self.infected
        except ZeroDivisionError:
            self.lethality = 0


class EverydayView(APIView):
    """
    List day registers 
    """

    def _get_register(self):
        registers = []

        try:
            day = SicksModel.objects.earliest('infection_identification_date').infection_identification_date
            last_day = SicksModel.objects.latest('infection_identification_date').infection_identification_date

            infected, dead, cont = 0, 0, 0
            while day <= last_day:
                register = RegisterDay(day, infected, dead)
                register.id = cont
                registers.append(register)
                infected, dead = register.infected, register.dead
                cont += 1
                day += timedelta(1)

        except SicksModel.DoesNotExist:
            pass

        return registers

    def get(self, request, format=None):

        serializer = EverydaySerializer(self._get_register(), many=True)
        return Response(serializer.data)

everyday_view = EverydayView.as_view()