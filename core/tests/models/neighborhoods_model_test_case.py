# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import CountysModel, NeighborhoodsModel

class NeighborhoodsModelTestCase(TestCase):
    """Class Testing Model NeighborhoodsModel """

    def setUp(self):
        """Initial Test Settings"""        
        self.county = mommy.make(CountysModel)
        self.neighborhood = mommy.make(NeighborhoodsModel, county= self.county)

    def tearDown(self):
        """Final method"""        
        self.county.delete() 
        self.neighborhood.delete()
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'county'] 

        for fild in filds:
            self.assertTrue(hasattr(NeighborhoodsModel, fild),
                            'Class NeighborhoodsModel does not have the field {}'.format(fild))

    def test_there_is_a_neighborhood(self):
        """test if you are creating a NeighborhoodsModel correctly"""
        
        self.assertEquals(NeighborhoodsModel.objects.count(), 1)
        
        neighborhood = NeighborhoodsModel.objects.all()[0]

        self.assertEquals(neighborhood.name, self.neighborhood.name)
        self.assertEquals(neighborhood.county, self.neighborhood.county)        

    def test_str_neighborhood(self):
        """test if str method of NeighborhoodsModel is correctly"""
        
        self.assertEquals(str(self.neighborhood), f'Neighborhood: {self.neighborhood.name} - {self.neighborhood.county.name} - {self.neighborhood.county.state.initial}')
        