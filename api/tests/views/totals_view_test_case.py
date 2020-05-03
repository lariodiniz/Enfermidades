# coding: utf-8
__author__ = "Lário dos Santos Diniz"


from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.conf import settings

from model_mommy import mommy

from core.models import SicksModel


class TotalsViewTestCase(APITestCase):
    """test Totals view"""
    def setUp(self):

        self.url = reverse('api:totals')
        mommy.make(SicksModel)

        self.client = APIClient()


    def tearDown(self):
        pass

    def test_totals_view_get_200(self):

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200,
                          'a get request for url "{}" is not returning status code 200'.format(self.url))        

