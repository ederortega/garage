from django.urls import reverse
from django.test import TestCase

# Create your tests here.
class TestSaleViews(TestCase):
    def test_homeview(self):
        url = reverse('sale:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
