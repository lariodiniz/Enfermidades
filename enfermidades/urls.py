# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin
from django.urls import path, include
from core.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name="index"),
    path('registro/', include('register.urls', namespace='register')),  
    path('api/', include('api.urls', namespace='api')),
]

