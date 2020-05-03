# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import AdressesModel, PersonsModel

class PersonsModelTestCase(TestCase):
    """Class Testing Model PersonsModel """

    def setUp(self):
        """Initial Test Settings"""
        self.address = mommy.make(AdressesModel)
        self.person = mommy.make(PersonsModel, address= self.address)

    def tearDown(self):
        """Final method"""
        self.address.delete()
        self.person.delete() 
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'address', 'date_of_death', 'age', 'age_range'] 

        for fild in filds:
            self.assertTrue(hasattr(PersonsModel, fild),
                            'Class PersonsModel does not have the field {}'.format(fild))

    def test_there_is_a_person(self):
        """test if you are creating a PersonsModel correctly"""
        
        self.assertEquals(PersonsModel.objects.count(), 1)
        
        person = PersonsModel.objects.all()[0]

        self.assertEquals(person.name, self.person.name)
        self.assertEquals(person.date_of_death, self.person.date_of_death)
        self.assertEquals(person.age, self.person.age)
        self.assertEquals(person.address, self.person.address)

    def test_str_person(self):
        """test if str method of PersonsModel is correctly"""
        
        self.assertEquals(str(self.person), f'{self.person.name}')