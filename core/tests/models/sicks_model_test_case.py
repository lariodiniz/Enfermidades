# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import PersonsModel, DiseasesModel, SicksModel

class SicksModelTestCase(TestCase):
    """Class Testing Model SicksModel """

    def setUp(self):
        """Initial Test Settings"""
        self.person = mommy.make(PersonsModel)
        self.disease = mommy.make(DiseasesModel)
        self.sick = mommy.make(SicksModel, person= self.person)

    def tearDown(self):
        """Final method"""
        self.person.delete()
        self.disease.delete()
        self.sick.delete() 
        

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['person', 'infection_date', 'infection_identification_date', 'disease', 'creation_date', 'update_date', 'origins'] 

        for fild in filds:
            self.assertTrue(hasattr(SicksModel, fild),
                            'Class SicksModel does not have the field {}'.format(fild))

    def test_there_is_a_sick(self):
        """test if you are creating a SicksModel correctly"""

        self.assertEquals(SicksModel.objects.count(), 1)

        sick = SicksModel.objects.all()[0]

        self.assertEquals(sick.infection_date, self.sick.infection_date)
        self.assertEquals(sick.infection_identification_date, self.sick.infection_identification_date)
        self.assertEquals(sick.creation_date, self.sick.creation_date)
        self.assertEquals(sick.update_date, self.sick.update_date)
        self.assertEquals(sick.person, self.sick.person)
        self.assertEquals(sick.disease, self.sick.disease)
        self.assertEquals(sick.origins, self.sick.origins)

    def test_str_sick(self):
        """test if str method of SicksModel is correctly"""

        self.assertEquals(str(self.sick), f'{self.sick.pk} - {self.sick.person.name}')