#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import AdressesModel

class PersonsModel(models.Model):
    """
     PersonsModel table model.     
    """   
    age_ranges =(
        (-1, _(u'Undefined')),
        (0, _(u'up to 10 years old')),
        (1, _(u'from 10 to 19 years old')),
        (2, _(u'from 20 to 29 years old')),
        (3, _(u'from 30 to 39 years old')),
        (4, _(u'from 40 to 49 years old')),
        (5, _(u'from 50 to 59 years old')),
        (6, _(u'from 60 to 69 years old')),
        (7, _(u'from 70 to 79 years old')),
        (8, _(u'over 80 years old')),
    )
    
    name = models.CharField(_('Name'),max_length=200)
    date_of_death = models.DateField(verbose_name=_('Date of death'), null=True) 
    age = models.PositiveIntegerField(verbose_name=_('Age'), null=True)
    age_range = models.IntegerField(verbose_name=_('Age range'), choices=age_ranges, default=-1) 
    address = models.ForeignKey(AdressesModel, verbose_name=_('Address'), on_delete=models.CASCADE)
    dead = models.BooleanField(_('Dead'), default=False)

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return str(_(f'{self.name}'))
   