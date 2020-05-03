# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import path

from register.views import ministry_of_health_view, manual_registration_view


app_name = 'register'

urlpatterns = [
    path('ministerio/', ministry_of_health_view, name='ministry_of_health'),
    path('ministerioManual/', manual_registration_view, name='manual_registration'),
]
