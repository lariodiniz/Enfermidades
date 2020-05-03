#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext_lazy as _

class UrlFontsModel(models.Model):
    """
     UrlFont table model.
     - Saves the font of the system data.
    """

    name = models.CharField(_('Name'),max_length=200)
    description = models.CharField(_('Description'), max_length=250, blank=True, null=True) 
    url = models.CharField(_('Url'),max_length=250)
    
    class Meta:
        verbose_name = _('Font')
        verbose_name_plural = _('Fonts')

    def __str__(self):
        return str(_(f'Font: {self.url}'))
   