from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import *
from .serializer import *

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_product(name="", description="", price="", img_url=""):
        if name != "" and description != "" and price != "":
            Products.objects.create(name=name, description=description, price=price, img_url=img_url)

    def setUp(self):
        # add test data
        self.add_product("laptop", "Dell inspiron", 200, "www.rty.com")
        self.add_product("Dennim", "Leather Jacket", 300, "https://tryie.com")
        

class GetAllProductsTest(BaseViewTest):

    def test_get_all_products(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("products")
        )
        # fetch the data from db
        expected = Products.objects.all()
        serialized = ProductsSerializer(expected, many=True)
        self.assertEqual(len(response.data), len(serialized.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class OderItemTest(BaseViewTest):
    
    def test_create_orderitem(self):
        response = self.client.get(
            reverse("products")
        )
        print(response.data)

        product = response.data[0]
        print(product)
        