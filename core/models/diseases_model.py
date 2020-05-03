#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

class DiseasesModel(models.Model):
    """
     Diseases table model.
     - Diseases.
    """

    name = models.CharField(_('Name'),max_length=200)
    
    class Meta:
        verbose_name = _('Disease')
        verbose_name_plural = _('Diseases')

    def __str__(self):
        return str(_(f'Disease: {self.name}'))
   