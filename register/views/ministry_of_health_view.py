#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from datetime import datetime

from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import (DiseasesModel, UrlFontsModel, OriginsModel, StatesModel,
    CountysModel, NeighborhoodsModel, AdressesModel, PersonsModel, SicksModel
    )


class MinistryOfHealthView(LoginRequiredMixin, TemplateView ):

    template_name = 'register/ministry_of_health.html'
    
    def register_sick(self, cidade, data, novosCasos, novosObitos):

        data = datetime.strptime(data, '%d/%m/%Y')
        novo = SicksModel.objects.filter(
            infection_identification_date=data, 
            person__address__neighborhood__county__state__initial__contains=cidade).count() 

        if novo < int(novosCasos):
            #print(f'Cadastrando: {cidade}, {data}, Novos: {novosCasos}, Obitos: {novosObitos}')
            try:
                estado = StatesModel.objects.get(initial = cidade)
            except StatesModel.DoesNotExist:
                print('não existe')

            try:
                cidade = CountysModel.objects.get(name = 'INDEFINIDO', state = estado)
            except CountysModel.DoesNotExist:
                cidade = CountysModel()
                cidade.name = 'INDEFINIDO'    
                cidade.state = estado
                cidade.save()

            try:
                bairro = NeighborhoodsModel.objects.get(name = 'INDEFINIDO', county = cidade)
            except NeighborhoodsModel.DoesNotExist:
                bairro = NeighborhoodsModel()
                bairro.name = 'INDEFINIDO'
                bairro.county = cidade
                bairro.save()        

            ''' 
            enderecos = []
            for x in range(int(novosCasos)):                        
                endereco = AdressesModel()
                endereco.streets = 'INDEFINIDO'       
                endereco.neighborhood = bairro
                enderecos.append(endereco)
            
            AdressesModel.objects.bulk_create(enderecos)

            pessoas = []
            obtos = int(novosObitos)
            for x in range(int(novosCasos)):                        
                pessoa = PersonsModel()
                pessoa.name = 'INDEFINIDO'    
                pessoa.address = enderecos[x]
                if obtos > 0:
                    pessoa.date_of_death = data
                    obtos -+ 1
                pessoas.append(pessoa)
            
            PersonsModel.objects.bulk_create(pessoas)
            
            passientes = []
            
            for x in range(int(novosCasos)):                        
                passiente = SicksModel()            
                passiente.infection_identification_date = data
                    
                passiente.person = pessoas[x]
                passiente.disease = self.disease
                
                passientes.append(passiente)
            
            SicksModel.objects.bulk_create(passientes)

            for x in passientes:
                x.origins.add(self.origin)

            '''

            obitos = int(novosObitos)
            for x in range(int(novosCasos) - novo):                        
                endereco = AdressesModel()
                endereco.streets = 'INDEFINIDO'       
                endereco.neighborhood = bairro
                endereco.save()

                pessoa = PersonsModel()
                pessoa.name = 'INDEFINIDO'    
                pessoa.address = endereco
                if obitos > 0:
                    pessoa.date_of_death = data
                    obitos -+ 1

                pessoa.save()
                passiente = SicksModel()
                passiente.infection_identification_date = data

                passiente.person = pessoa
                passiente.disease = self.disease
                passiente.save()
                passiente.origins.add(self.origin)
                novo += 1


    def get(self, request, *args, **kwargs):
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        self.disease = DiseasesModel.objects.get(name = 'SARS-CoV-2')
        self.font = UrlFontsModel.objects.get(name = 'Ministério da Saude')

        csv_file = request.FILES['planilha']
        '''
        CountysModel.objects.all().delete()
        NeighborhoodsModel.objects.all().delete()
        AdressesModel.objects.all().delete()
        PersonsModel.objects.all().delete()
        SicksModel.objects.all().delete()
        OriginsModel.objects.all().delete()
        '''
        #if not csv_file.name.endswith('.csv'):
        #    messages.error(request, 'THIS IS NOT A CSV FILE')

        print('Iniciando Importação')
        data_set = csv_file.read().decode("utf-8")

        lines = data_set.split("\n")
        lines = lines[1:-1]
        if len(lines) > 0:
            
            self.origin = OriginsModel()
            self.origin.font = self.font  
            self.origin.save()
        
        
        for line in lines:            
            if line != '':
                fields = line.split(";")
                self.register_sick(fields[1], fields[2], fields[3], fields[5])
		
        print('Finalizada Importação')

        return render(request, self.template_name)

ministry_of_health_view = MinistryOfHealthView.as_view()

