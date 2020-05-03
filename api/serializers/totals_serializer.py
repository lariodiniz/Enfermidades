#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from rest_framework import serializers

class TotalsSerializer(serializers.Serializer):
    last_update = serializers.DateField()
    infected =  serializers.IntegerField()
    dead =  serializers.IntegerField()
    lethality =  serializers.DecimalField(decimal_places=2, max_digits=5)


