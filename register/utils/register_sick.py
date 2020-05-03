#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from datetime import datetime, timedelta

from django.db.models import Sum

from core.models import (DiseasesModel, UrlFontsModel, OriginsModel, StatesModel,
    CountysModel, NeighborhoodsModel, AdressesModel, PersonsModel, SicksModel
    )


class RegisterSick:


    def __init__(self, disease, font):
        self._disease = DiseasesModel.objects.get(name = disease)
        self._font = UrlFontsModel.objects.get(name = font)
        self._origin = OriginsModel()
        self._origin.font = self._font
        self._origin.save()

    def register_total(self, estado, data, casos, obitos):

        
        existe = SicksModel.objects.filter(
            infection_identification_date__lte=data+timedelta(1),
            person__address__neighborhood__county__state__initial__contains=estado).count()

        novosInfectados = casos - existe

        existe = SicksModel.objects.filter(
            infection_identification_date__lte=data+timedelta(1),
            person__dead=True,
            person__address__neighborhood__county__state__initial__contains=estado).count()

        novosObitos = obitos - existe

        if novosInfectados > 0:
            self.register(estado, data, casos, novosObitos)
            print(f'Cadastrados {novosInfectados} novos infectados')
            return novosInfectados, novosObitos

        return 0, 0

    def register(self, estado, data, novosCasos, novosObitos):

        novo = SicksModel.objects.filter(
            infection_identification_date=data,
            person__address__neighborhood__county__state__initial__contains=estado).count() 

        if novo < int(novosCasos):
            try:
                estado = StatesModel.objects.get(initial = estado)
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
                    pessoa.dead = True
                    pessoa.date_of_death = data
                    obitos -= 1
                else:
                    pessoa.dead = False
                    pessoa.date_of_death = None

                pessoa.save()
                passiente = SicksModel()
                passiente.infection_identification_date = data

                passiente.person = pessoa
                passiente.disease = self._disease
                passiente.save()
                passiente.origins.add(self._origin)
                novo += 1


