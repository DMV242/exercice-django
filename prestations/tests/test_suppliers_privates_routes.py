from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Supplier
from ..serializers import SupplierSerializer
from django.contrib.auth import get_user_model
from .test_urls import *


class PrivateSupplierTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test@gmail.com", "testpass")
        self.client.force_authenticate(self.user)

    def test_create_supplier(self):
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@gmail.com",
            "company_name": "Doe Inc",
        }

        res = self.client.post(SUPPLIER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        data = SupplierSerializer(res.data).data
        self.assertEqual(data["first_name"], payload["first_name"])
        self.assertEqual(data["last_name"], payload["last_name"])
        self.assertEqual(data["email"], payload["email"])

    def test_delete_supplier(self):
        supplier = Supplier.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            company_name="Doe Inc",
        )

        res = self.client.delete(detail_url_supplier(supplier.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_retreive_detail_supplier(self):
        supplier = Supplier.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            company_name="Doe Inc",
        )

        res = self.client.get(detail_url_supplier(supplier.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = SupplierSerializer(res.data).data
        self.assertEqual(data["first_name"], supplier.first_name)
        self.assertEqual(data["last_name"], supplier.last_name)

    def test_partial_update_supplier(self):
        supplier = Supplier.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            company_name="Doe Inc",
        )

        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
        }
        res = self.client.patch(detail_url_supplier(supplier.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = SupplierSerializer(res.data).data
        self.assertEqual(data["first_name"], payload["first_name"])
        self.assertEqual(data["last_name"], payload["last_name"])

    def test_full_update_supplier(self):
        supplier = Supplier.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@gmail.com",
            company_name="Doe Inc",
        )

        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@gmail.com",
            "company_name": "Jane Inc ",
        }
        res = self.client.put(detail_url_supplier(supplier.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = SupplierSerializer(res.data).data
        self.assertEqual(data["first_name"], payload["first_name"])
        self.assertEqual(data["last_name"], payload["last_name"])
