# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import NeighborhoodsModel, AdressesModel

class AdressesModelTestCase(TestCase):
    """Class Testing Model AdressesModel """

    def setUp(self):
        """Initial Test Settings"""        
        self.neighborhood = mommy.make(NeighborhoodsModel)
        self.address = mommy.make(AdressesModel, neighborhood= self.neighborhood)
        

    def tearDown(self):
        """Final method"""        
        self.neighborhood.delete() 
        self.address.delete()
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['streets', 'complement', 'number', 'cep', 'neighborhood'] 

        for fild in filds:
            self.assertTrue(hasattr(AdressesModel, fild),
                            'Class AdressesModel does not have the field {}'.format(fild))

    def test_there_is_a_address(self):
        """test if you are creating a AdressesModel correctly"""
        
        self.assertEquals(AdressesModel.objects.count(), 1)
        
        address = AdressesModel.objects.all()[0]

        self.assertEquals(address.streets, self.address.streets)
        self.assertEquals(address.complement, self.address.complement)
        self.assertEquals(address.number, self.address.number)
        self.assertEquals(address.cep, self.address.cep)
        self.assertEquals(address.neighborhood, self.address.neighborhood)        

    def test_str_address(self):
        """test if str method of AdressesModel is correctly"""
        
        self.assertEquals(str(self.address), f'Address: {self.address.streets} - {self.address.neighborhood.name} - {self.address.neighborhood.county.name} - {self.address.neighborhood.county.state.initial}')
        