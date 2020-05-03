# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import StatesModel, CountysModel

class CountysModelTestCase(TestCase):
    """Class Testing Model CountysModel """

    def setUp(self):
        """Initial Test Settings"""
        self.state = mommy.make(StatesModel)
        self.county = mommy.make(CountysModel, state= self.state)

    def tearDown(self):
        """Final method"""
        self.state.delete()
        self.county.delete() 
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'foundation', 'state'] 

        for fild in filds:
            self.assertTrue(hasattr(CountysModel, fild),
                            'Class CountysModel does not have the field {}'.format(fild))

    def test_there_is_a_county(self):
        """test if you are creating a CountysModel correctly"""
        
        self.assertEquals(CountysModel.objects.count(), 1)
        
        county = CountysModel.objects.all()[0]

        self.assertEquals(county.name, self.county.name)
        self.assertEquals(county.foundation, self.county.foundation)
        self.assertEquals(county.state, self.county.state)

    def test_str_county(self):
        """test if str method of CountysModel is correctly"""
        
        self.assertEquals(str(self.county), f'Countys: {self.county.name} - {self.county.state.initial}')