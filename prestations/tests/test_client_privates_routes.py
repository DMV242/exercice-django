from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Client
from ..serializers import ClientSerializer
from django.contrib.auth import get_user_model
from .test_urls import *


class PrivateClientTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test@gmail.com", "testpass")
        self.client.force_authenticate(self.user)

    def test_create_client(self):
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@gmail.com",
        }

        res = self.client.post(CLIENT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        data = ClientSerializer(res.data).data
        self.assertEqual(data["first_name"], payload["first_name"])
        self.assertEqual(data["last_name"], payload["last_name"])
        self.assertEqual(data["email"], payload["email"])

    def test_retreive_detail_client(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        res = self.client.get(detail_url_client(client.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = ClientSerializer(res.data).data
        self.assertEqual(data["first_name"], client.first_name)
        self.assertEqual(data["last_name"], client.last_name)

    def test_partial_update_client(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
        }
        res = self.client.patch(detail_url_client(client.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = ClientSerializer(res.data).data
        self.assertEqual(data["first_name"], payload["first_name"])
        self.assertEqual(data["last_name"], payload["last_name"])

    def test_full_update_client(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        payload = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@gmail.com",
        }
        res = self.client.put(detail_url_client(client.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = ClientSerializer(res.data).data
        self.assertEqual(data["first_name"], payload["first_name"])
        self.assertEqual(data["last_name"], payload["last_name"])
