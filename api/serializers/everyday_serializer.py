#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from rest_framework import serializers
from core.models import GeneralDataModel

class EverydaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDataModel
        fields = ['pk', 'day','infecteds', 'infected_porcents',
        'infected_news','infected_news_porcents','deads',
        'dead_porcents','dead_news','dead_news_porcents', 'lethality'
        ]

'''
class TresDeTEspecializacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especializacoes
        fields = ['id','name', 'description']
'''
