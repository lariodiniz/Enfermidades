#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import StatesModel

class CountysModel(models.Model):
    """
     CountysModel table model.
     - brazilian Countys.
    """   
    
    name = models.CharField(_('Name'),max_length=200)
    foundation = models.DateField(verbose_name=_('Foundation'), null=True) 
    state = models.ForeignKey(StatesModel, verbose_name=_('State'), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('County')
        verbose_name_plural = _('Countys')

    def __str__(self):
        return str(_(f'Countys: {self.name} - {self.state.initial}'))
   