# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import UrlFontsModel, OriginsModel

class OriginsModelTestCase(TestCase):
    """Class Testing Model OriginsModel """

    def setUp(self):
        """Initial Test Settings"""
        self.url_font = mommy.make(UrlFontsModel)
        self.origin = mommy.make(OriginsModel, font=self.url_font)

    def tearDown(self):
        """Final method"""
        self.url_font.delete()
        self.origin.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['kind', 'font', 'date'] 

        for fild in filds:
            self.assertTrue(hasattr(OriginsModel, fild),
                            'Class OriginsModel does not have the field {}'.format(fild))

    def test_there_is_a_origin(self):
        """test if you are creating a OriginsModel correctly"""
        
        self.assertEquals(OriginsModel.objects.count(), 1)
        
        origin = OriginsModel.objects.all()[0]

        self.assertEquals(origin.kind, self.origin.kind)
        self.assertEquals(origin.date, self.origin.date)
        self.assertEquals(origin.font, self.origin.font)
        self.assertEquals(origin.font, self.url_font)

    def test_str_origin(self):
        """test if str method of OriginsModel is correctly"""
        self.assertEquals(str(self.origin), f'Origin: {self.origin.font.name} - {self.origin.date}')