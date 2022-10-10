from django.test import TestCase, RequestFactory
from .views import *
# Create your tests here.

class FirstTest(TestCase):
    def setUp(self):
        self._factory = RequestFactory()
    def test_first(self):
        request = self._factory.get("/mainapp/")
        response = index(request)
        self.assertEqual(response.status_code, 200)
