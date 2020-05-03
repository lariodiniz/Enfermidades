# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import GeneralDataModel

class GeneralDataModelTestCase(TestCase):
    """Class Testing Model GeneralDataModel """

    def setUp(self):
        """Initial Test Settings"""
        self.general = mommy.make(GeneralDataModel)

    def tearDown(self):
        """Final method"""
        self.general.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['day', 'infected_news', 'dead_news', 'disease', 'infecteds', 
                'infected_porcents', 'infected_news_porcents', 'deads', 'dead_porcents', 
                'dead_news_porcents', 'lethality']

        for fild in filds:
            self.assertTrue(hasattr(GeneralDataModel, fild),
                            'Class GeneralDataModel does not have the field {}'.format(fild))

    def test_there_is_a_generalData(self):
        """test if you are creating a GeneralDataModel correctly"""

        self.assertEquals(GeneralDataModel.objects.count(), 1)

        general = GeneralDataModel.objects.all()[0]

        self.assertEquals(general.day, self.general.day)
        self.assertEquals(general.infected_news, self.general.infected_news)
        self.assertEquals(general.dead_news, self.general.dead_news)
        self.assertEquals(general.disease, self.general.disease)
        self.assertEquals(general.infecteds, self.general.infecteds)
        self.assertEquals(general.infected_porcents, self.general.infected_porcents)
        self.assertEquals(general.infected_news_porcents, self.general.infected_news_porcents)
        self.assertEquals(general.deads, self.general.deads)
        self.assertEquals(general.dead_porcents, self.general.dead_porcents)
        self.assertEquals(general.dead_news_porcents, self.general.dead_news_porcents)
        self.assertEquals(general.lethality, self.general.lethality)


    def test_str_generalData(self):
        """test if str method of GeneralDataModel is correctly"""

        self.assertEquals(str(self.general),
                        str(f'{self.general.disease.name}: {self.general.day:%d/%m/%Y} - New infecteds: {self.general.infected_news} | New deads: {self.general.dead_news}'))