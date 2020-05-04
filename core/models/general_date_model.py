#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from core.models import DiseasesModel

class GeneralDataModel(models.Model):
    """
     GeneralDataModel table model.
    """

    day = models.DateField(verbose_name=_('Day'))
    infected_news = models.IntegerField(verbose_name=_('Infected News'))
    dead_news = models.IntegerField(verbose_name=_('Dead News'))

    disease = models.ForeignKey(DiseasesModel, verbose_name=_('Disease'), on_delete=models.CASCADE)

    @property
    def _brazil_population(self):
        return 211462943

    @property
    def infecteds(self):
        infect = GeneralDataModel.objects.filter(day__lte=self.day)
        total = 0
        for i in infect:
            total += i.infected_news 
        return total

    def _media(self, number1, number2):
        try:
            n = (number1 * 100) / number2
            n = float(f'{n:.2f}')
            return n
        except ZeroDivisionError:
            return 0

    @property
    def infected_porcents(self):
        return self._media(self.infecteds, self._brazil_population)

    @property
    def infected_news_porcents(self):
        return self._media(self.infected_news, self.infecteds)

    @property
    def deads(self):
        infect = GeneralDataModel.objects.filter(day__lte=self.day)
        total = 0
        for i in infect:
            total += i.dead_news

        return total

    @property
    def dead_porcents(self):
        return self._media(self.deads, self._brazil_population)

    @property
    def dead_news_porcents(self):
        return self._media(self.dead_news, self.deads)

    @property
    def lethality(self):
        return self._media(self.deads, self.infecteds)

    class Meta:
        verbose_name = _('General Data')
        verbose_name_plural = _('Generals Data')

    def __str__(self):
        return str(f'{self.disease.name}: {self.day:%d/%m/%Y} - New infecteds: {self.infected_news} | New deads: {self.dead_news}')
