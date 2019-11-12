from django.test import TestCase
from rest_framework.test import APITestCase
from store.models import Product

# Create your tests here.
class ProductCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count()
        product_attrs = {
            'name': 'New Product',
            'description': 'Awesome Product',
            'price': '123,45',
        }
        response = self.client.post('api/v1/products/new', product_attrs)
