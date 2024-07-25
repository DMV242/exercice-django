from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Prestation, Client, Supplier
from faker import Faker
from .test_urls import *


class PublicTest(TestCase):
    """
    This class tests that users have access to get routes even if they are not authenticated,
    and that they do not have access to POST,
    GET and delete routes if they are not authenticated.
    """

    def setUp(self):
        fake = Faker()
        clients = [
            Client.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
            )
            for _ in range(5)
        ]

        suppliers = [
            Supplier.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                company_name=fake.company(),
            )
            for _ in range(5)
        ]

        prestations = [
            Prestation.objects.create(
                client=fake.random_element(clients),
                supplier=fake.random_element(suppliers),
                offer_price=fake.random_number(digits=5),
                service_fee=fake.random_number(digits=3),
                status_client=fake.random_element(
                    [
                        "Action requise",
                        "Attendre",
                        "Terminé",
                        "Annulé",
                        "Confirme",
                        "En attente",
                        "Waiting Approval",
                    ]
                ),
                status_supplier=fake.random_element(
                    [
                        "Action requise",
                        "Attendre",
                        "Terminé",
                        "Annulé",
                        "Confirme",
                        "En attente",
                        "Waiting Approval",
                    ]
                ),
                type_prestation=fake.word(),
                charge_id=fake.unique.uuid4(),
                refund_id=fake.unique.uuid4(),
                charge_capture=fake.boolean(),
            )
            for _ in range(10)
        ]
        self.client = APIClient()

    def test_retrieve_prestations(self):
        """Test function to retrieve prestations"""
        res = self.client.get(PRESTATION_URL)
        self.assertEqual(len(res.data["results"]), 10)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_clients(self):
        """Test function to retrieve all clients"""
        res = self.client.get(CLIENT_URL)
        self.assertEqual(len(res.data["results"]), 5)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_suppliers(self):
        """Test function to retrieve all suppliers"""
        res = self.client.get(SUPPLIER_URL)
        self.assertEqual(len(res.data["results"]), 5)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_request_on_private_route(self):
        """It should not be possible to make a post request on a private route"""
        res = self.client.post(PRESTATION_URL)
        res2 = self.client.post(CLIENT_URL)
        res3 = self.client.post(SUPPLIER_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res3.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_request_on_private_route(self):
        """It should not be possible to make a post request on a private route"""
        res = self.client.patch(PRESTATION_URL)
        res2 = self.client.patch(CLIENT_URL)
        res3 = self.client.patch(SUPPLIER_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res3.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_request_on_private_route(self):
        """It should not be possible to make a post request on a private route"""
        res = self.client.delete(PRESTATION_URL)
        res2 = self.client.delete(CLIENT_URL)
        res3 = self.client.delete(SUPPLIER_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res2.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res3.status_code, status.HTTP_401_UNAUTHORIZED)
