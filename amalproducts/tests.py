from django.test import TestCase
from amalproducts.models import Product

# Create your tests here.

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="mouse", product_number=1, stock=5, price=2.00)
        Product.objects.create(name="notebook", product_number=2, stock=4, price=3.00)

    def test_products_integrity(self):
        mouse = Product.objects.get(name="mouse")
        notebook = Product.objects.get(name="notebook")
        self.assertEqual(1, mouse.product_number)
        self.assertEqual(5, mouse.stock)
        self.assertEqual(2.00, mouse.price)

        self.assertEqual(2, notebook.product_number)
        self.assertEqual(4, notebook.stock)
        self.assertEqual(3.00, notebook.price)
        