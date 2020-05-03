# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import DiseasesModel

class DiseasesModelTestCase(TestCase):
    """Class Testing Model  Diseases """

    def setUp(self):
        """Initial Test Settings"""        
        self.disease = mommy.make(DiseasesModel)       
        

    def tearDown(self):
        """Final method"""                
        self.disease.delete()
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name'] 

        for fild in filds:
            self.assertTrue(hasattr(DiseasesModel, fild),
                            'Class DiseasesModel does not have the field {}'.format(fild))

    def test_there_is_a_disease(self):
        """test if you are creating a DiseasesModel correctly"""
        
        self.assertEquals(DiseasesModel.objects.count(), 1)
        
        disease = DiseasesModel.objects.all()[0]

        self.assertEquals(disease.name, self.disease.name)     

    def test_str_disease(self):
        """test if str method of DiseasesModel is correctly"""
        
        self.assertEquals(str(self.disease), f'Disease: {self.disease.name}')
        