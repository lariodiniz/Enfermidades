#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import PersonsModel, DiseasesModel, OriginsModel

class SicksModel(models.Model):
    """
     SicksModel table model.
    """   

    infection_date = models.DateField(verbose_name=_('Infection date'), null=True) 
    infection_identification_date = models.DateField(verbose_name=_('Infection identification date'), null=True)
    creation_date = models.DateField(verbose_name=_('Creation date'), auto_now_add=True)
    update_date = models.DateField(verbose_name=_('Creation date'), auto_now=True)

    person = models.ForeignKey(PersonsModel, verbose_name=_('Person'), on_delete=models.CASCADE)
    disease = models.ForeignKey(DiseasesModel, verbose_name=_('Disease'), on_delete=models.CASCADE)
    origins = models.ManyToManyField(OriginsModel, verbose_name=_('Origins'))
    
    class Meta:
        verbose_name = _('Sick')
        verbose_name_plural = _('Sicks')

    def __str__(self):
        return str(_(f'{self.pk} - {self.person.name}'))
   