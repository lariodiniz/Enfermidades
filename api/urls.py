# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import path

from api.views import totals_view, everyday_view


app_name = 'api'

urlpatterns = [
    path('totais/', totals_view, name='totals') ,
    path('diario/', everyday_view, name='everyday') ,
]