from django.test import TestCase, Client
from amalproducts.models import Product
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from amalproducts.serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


# Create your tests here.

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="mouse", product_number=1, stock=5, price=2.00)
        Product.objects.create(name="notebook", product_number=2, stock=4, price=3.00)
        self.factory = APIRequestFactory()
        self.client = Client()
        self.credentials = {
            'username': 'admin',
            'password': 'password123'
        }
        self.client.login(username='admin', password='password123')
        self.user = User.objects.create_user(**self.credentials)
        product_with_owner = Product.objects.create(name="cable", product_number=3, stock=3, price=2.50)
        product_with_owner.owner.add(self.user)

    def test_integrity(self):
        mouse = Product.objects.get(name="mouse")
        notebook = Product.objects.get(name="notebook")
        self.assertEqual(1, mouse.product_number)
        self.assertEqual(5, mouse.stock)
        self.assertEqual(2.00, mouse.price)

        self.assertEqual(2, notebook.product_number)
        self.assertEqual(4, notebook.stock)
        self.assertEqual(3.00, notebook.price)
    
    def test_products_authorization(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        self.assertEqual(200, response.status_code)
    
    def test_products_endpoint(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + response.data["token"],
        }
        # headers2 = {'Authorization': 'Token ' + response.data["token"]}
        response2 = self.client.get('/1/products/', **auth_headers)
        self.assertEqual(200, response2.status_code)

    def test_products_favourites_endpoint(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + response.data["token"],
        }
        # headers2 = {'Authorization': 'Token ' + response.data["token"]}
        response2 = self.client.get('/1/products/favourites/', **auth_headers)
        self.assertEqual(200, response2.status_code)

    def test_product_mark_as_favourite_endpoint(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + response.data["token"],
        }
        # headers2 = {'Authorization': 'Token ' + response.data["token"]}
        response2 = self.client.get('/1/products/1/mark_as_favourite/', **auth_headers)
        self.assertEqual(200, response2.status_code)
  
    def test_products_integrity(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + response.data["token"],
        }
        response2 = self.client.get('/1/products/', **auth_headers).json()
        for idx, json in enumerate(response2):
            serializer = ProductSerializer(Product.objects.get(pk=idx+1))
            self.assertDictEqual(json, serializer.data)

    def test_products_favourite_integrity(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + response.data["token"],
        }
        response2 = self.client.get('/1/products/favourites/', **auth_headers).json()
        for json in response2:
            serializer = ProductSerializer(Product.objects.get(name="cable"))
            self.assertDictEqual(json, serializer.data)

    def test_marking_product_integrity(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = self.client.post('/1/login/', data=self.credentials, headers=headers)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + response.data["token"],
        }
        self.client.get('/1/products/1/mark_as_favourite/', **auth_headers)
        response3 = self.client.get('/1/products/favourites/', **auth_headers).json()
        mouse = ProductSerializer(Product.objects.get(name="mouse")).data
        cable = ProductSerializer(Product.objects.get(name="cable")).data
        self.assertIn(mouse, list(response3))
        self.assertIn(cable, list(response3))
        self.assertEqual(len(list(response3)), 2)