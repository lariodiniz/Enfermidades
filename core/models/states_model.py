#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

class StatesModel(models.Model):
    """
     StatesModel table model.
     - States of the brazilian union.
    """   
    

    regions = (
        (0, _(u'North')),
        (1, _(u'Northeast')),
        (2, _(u'Midwest')),
        (3, _(u'Southeast')),
        (4, _(u'South')),
    )
    
    name = models.CharField(_('Name'),max_length=200)
    initial = models.CharField(_('Initial'),max_length=2, unique=True)
    region = models.IntegerField(verbose_name=_('Region'), choices=regions)  
    
    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')

    def __str__(self):
        return str(_(f'States: {self.name} - {self.region}'))
   