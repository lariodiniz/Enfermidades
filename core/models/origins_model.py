#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UrlFontsModel


class OriginsModel(models.Model):
    """
     OriginsModel table model.
     - Saves the origin of the system data.
    """
    
    kinds = (
        ('C', _(u'Create')),
        ('U', _(u'Update'))
    )
    
    kind = models.CharField(verbose_name=_('Kind'), max_length=1, choices=kinds, default='C')  
    font = models.ForeignKey(UrlFontsModel, verbose_name=_('Font'), on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_('Date'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('Origin')
        verbose_name_plural = _('Origins')        

    def __str__(self):
        return str(_(f'Origin: {self.font.name} - {self.date}'))
   