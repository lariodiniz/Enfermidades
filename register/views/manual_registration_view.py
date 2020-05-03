#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from core.models import (DiseasesModel, UrlFontsModel, OriginsModel, StatesModel,
    CountysModel, NeighborhoodsModel, AdressesModel, PersonsModel, SicksModel
    )

from register.utils import RegisterSick

class ManualRegistrationView(LoginRequiredMixin, TemplateView ):

    template_name = 'register/manual_registration.html'
    def get(self, request, *args, **kwargs):
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        if 'inputInfectados' not in request.POST.keys() or \
            'inputMortos' not in request.POST.keys() or \
            'inputData' not in request.POST.keys():
            messages.add_message(request, messages.WARNING, 'Erro no formulario de importação')
            return render(request, self.template_name)

        try:
            novosCasos = int(request.POST['inputInfectados'])
        except ValueError:
            messages.add_message(request, messages.WARNING, 'O campo Total de Infectados precisa ter um numero')
            return render(request, self.template_name)

        if novosCasos == -100:
            CountysModel.objects.all().delete()
            NeighborhoodsModel.objects.all().delete()
            AdressesModel.objects.all().delete()
            PersonsModel.objects.all().delete()
            SicksModel.objects.all().delete()
            OriginsModel.objects.all().delete()
            messages.add_message(request, messages.SUCCESS, 'Todos Os registros apagados')
            return render(request, self.template_name)

        try:
            novosObitos = int(request.POST['inputMortos'])
        except ValueError:
            messages.add_message(request, messages.WARNING, 'O campo Total Mortos precisa ter um numero')
            return render(request, self.template_name)

        if novosCasos < 0:
            messages.add_message(request, messages.WARNING, 'O campo Total de Infectados precisa ser positivo')
            return render(request, self.template_name)

        if novosObitos < 0:
            messages.add_message(request, messages.WARNING, 'O campo Total Mortos precisa ser positivo')
            return render(request, self.template_name)

        try:
            data =request.POST['inputData']
            data = datetime.strptime(f'{data[8:10]}/{data[5:7]}/{data[0:4]}', '%d/%m/%Y')
        except ValueError:
            messages.add_message(request, messages.WARNING, 'O campo Data precisa ser definido')
            return render(request, self.template_name)

        registrar = RegisterSick('SARS-CoV-2', 'Ministério da Saude')

        infectados, obitos = registrar.register_total('IN', data, novosCasos, novosObitos)
        messages.add_message(request, messages.SUCCESS, f'Dados cadastrados no dia {data:%d/%m/%Y-}. {infectados} novos infectados e {obitos} novos mortos.')

        return render(request, self.template_name)

manual_registration_view = ManualRegistrationView.as_view()

