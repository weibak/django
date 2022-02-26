import pytest
from django.test import Client
from faker import Faker

from shop.models import Purchase

faker = Faker()


@pytest.mark.django_db
class TestShopApi:
    def test_shop_api(self):
        client = Client()

        response = client.get("/api/shop/")
        assert response.status_code == 200

