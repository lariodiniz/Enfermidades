#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.contrib import admin

from .models import (DiseasesModel, UrlFontsModel, OriginsModel, StatesModel,
    CountysModel, NeighborhoodsModel, AdressesModel, PersonsModel, SicksModel
    )

class SicksAdmin(admin.ModelAdmin):

    list_display = ['person', 'infection_identification_date', 'state']
    date_hierarchy = 'infection_identification_date'
    def state(self, obj):
        return obj.person.address.neighborhood.county.state.initial

    search_fields = ['person']
    list_filter = ['infection_identification_date']

class PersonsAdmin(admin.ModelAdmin):

    list_display = ['name', 'age_range', 'dead', 'date_of_death', 'state']

    def state(self, obj):
        return obj.address.neighborhood.county.state.initial


    search_fields = ['name']
    list_filter = ['name', 'age_range', 'dead']

admin.site.register(DiseasesModel)
admin.site.register(UrlFontsModel)
admin.site.register(OriginsModel)
admin.site.register(StatesModel)
admin.site.register(CountysModel)
admin.site.register(NeighborhoodsModel)
admin.site.register(AdressesModel)
admin.site.register(PersonsModel, PersonsAdmin)
admin.site.register(SicksModel, SicksAdmin)
