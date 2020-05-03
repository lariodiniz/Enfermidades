# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import UrlFontsModel

class UrlFontsModelTestCase(TestCase):
    """Class Testing Model UrlFont """

    def setUp(self):
        """Initial Test Settings"""
        self.url_font = mommy.make(UrlFontsModel)

    def tearDown(self):
        """Final method"""
        self.url_font.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'url', 'description']

        for fild in filds:
            self.assertTrue(hasattr(UrlFontsModel, fild),
                            'Class UrlFontsModel does not have the field {}'.format(fild))

    def test_there_is_a_url_font(self):
        """test if you are creating a UrlFontsModel correctly"""
        self.assertEquals(UrlFontsModel.objects.count(), 1)
        self.assertEquals(UrlFontsModel.objects.all()[0].description, self.url_font.description)

    def test_str_county(self):
        """test if str method of UrlFontsModel is correctly"""        
        self.assertEquals(str(self.url_font), f'Font: {self.url_font.url}')