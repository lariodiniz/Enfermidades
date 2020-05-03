#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import NeighborhoodsModel

class AdressesModel(models.Model):
    """
     AdressesModel table model.
     - brazilian Adresses.
    """   
    
    streets = models.CharField(_('Streets'),max_length=200)    
    complement = models.CharField(_('Complement'),max_length=100, null=True)   
    number = models.CharField(_('Number'),max_length=100, null=True)     
    cep = models.CharField(_('CEP'),max_length=8, null=True) 
    neighborhood = models.ForeignKey(NeighborhoodsModel, verbose_name=_('Neighborhood'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Adresses')

    def __str__(self):
        return str(_(f'Address: {self.streets} - {self.neighborhood.name} - {self.neighborhood.county.name} - {self.neighborhood.county.state.initial}'))
   