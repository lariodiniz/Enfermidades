#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from rest_framework import serializers

class EverydaySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    day = serializers.DateField()
    infected = serializers.IntegerField()
    infected_porcents = serializers.DecimalField(decimal_places=2, max_digits=5)
    infected_news = serializers.IntegerField()
    infected_news_porcents = serializers.DecimalField(decimal_places=2, max_digits=5)
    dead =  serializers.IntegerField()
    dead_porcents = serializers.DecimalField(decimal_places=2, max_digits=5)
    dead_news =  serializers.IntegerField()
    dead_news_porcents =  serializers.DecimalField(decimal_places=2, max_digits=5)
    lethality =  serializers.DecimalField(decimal_places=2, max_digits=5)
