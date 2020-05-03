#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import CountysModel

class NeighborhoodsModel(models.Model):
    """
     NeighborhoodsModel table model.
     - brazilian neighborhoods.
    """   
    
    name = models.CharField(_('Name'),max_length=200)    
    county = models.ForeignKey(CountysModel, verbose_name=_('County'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('Neighborhood')
        verbose_name_plural = _('Neighborhood')

    def __str__(self):
        return str(_(f'Neighborhood: {self.name} - {self.county.name} - {self.county.state.initial}'))
   