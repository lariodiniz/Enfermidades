# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import StatesModel

class StatesModelTestCase(TestCase):
    """Class Testing Model StatesModel """

    def setUp(self):
        """Initial Test Settings"""
        self.state = mommy.make(StatesModel)

    def tearDown(self):
        """Final method"""
        self.state.delete()
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'initial', 'region'] 

        for fild in filds:
            self.assertTrue(hasattr(StatesModel, fild),
                            'Class StatesModel does not have the field {}'.format(fild))

    def test_there_is_a_state(self):
        """test if you are creating a StatesModel correctly"""
        
        self.assertEquals(StatesModel.objects.count(), 1)
        
        state = StatesModel.objects.all()[0]

        self.assertEquals(state.name, self.state.name)
        self.assertEquals(state.initial, self.state.initial)
        self.assertEquals(state.region, self.state.region)

    def test_str_county(self):
        """test if str method of StatesModel is correctly"""
        self.assertEquals(str(self.state), f'States: {self.state.name} - {self.state.region}')