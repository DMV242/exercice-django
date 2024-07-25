from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Prestation, Client, Supplier
from ..serializers import PrestationSerializer
from django.contrib.auth import get_user_model
from .test_urls import *


class PrivateClientTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user("test@gmail.com", "testpass")
        self.client.force_authenticate(self.user)

    def test_create_prestation(self):

        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        supplier = Supplier.objects.create(
            first_name="David",
            last_name="Mvoula",
            email="davidmvoula@gmail.com",
            company_name="Mvoula Inc",
        )

        payload = {
            "offer_price": "100.00",
            "service_fee": "20.00",
            "status_client": "Action requise",
            "status_supplier": "Action requise",
            "type_prestation": "Informatique",
            "charge_id": "12",
            "refund_id": "34",
            "charge_capture": False,
            "client": client.id,
            "supplier": supplier.id,
        }

        res = self.client.post(PRESTATION_URL, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        prestation = Prestation.objects.get(id=res.data["id"])

        data = PrestationSerializer(prestation).data
        self.assertEqual(data["type_prestation"], payload["type_prestation"])
        self.assertEqual(data["status_supplier"], payload["status_supplier"])

    def test_retreive_detail_prestation(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        supplier = Supplier.objects.create(
            first_name="David",
            last_name="Mvoula",
            email="davidmvoula@gmail.com",
            company_name="Mvoula Inc",
        )

        prestation = Prestation.objects.create(
            client=client,
            supplier=supplier,
            offer_price="100.00",
            service_fee="20.00",
            status_client="Action requise",
            status_supplier="Action requise",
            type_prestation="Informatique",
            charge_id="12",
            refund_id="34",
            charge_capture=False,
        )

        res = self.client.get(detail_url_prestation(prestation.id), format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["id"], prestation.id)

    def test_delete_detail_prestation(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        supplier = Supplier.objects.create(
            first_name="David",
            last_name="Mvoula",
            email="davidmvoula@gmail.com",
            company_name="Mvoula Inc",
        )

        prestation = Prestation.objects.create(
            client=client,
            supplier=supplier,
            offer_price="100.00",
            service_fee="20.00",
            status_client="Action requise",
            status_supplier="Action requise",
            type_prestation="Informatique",
            charge_id="12",
            refund_id="34",
            charge_capture=False,
        )

        res = self.client.delete(detail_url_prestation(prestation.id), format="json")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_partial_update_prestation(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )

        supplier = Supplier.objects.create(
            first_name="David",
            last_name="Mvoula",
            email="davidmvoula@gmail.com",
            company_name="Mvoula Inc",
        )

        prestation = Prestation.objects.create(
            client=client,
            supplier=supplier,
            offer_price="100.00",
            service_fee="20.00",
            status_client="Action requise",
            status_supplier="Action requise",
            type_prestation="Informatique",
            charge_id="12",
            refund_id="34",
            charge_capture=False,
        )

        payload = {
            "offer_price": "200.00",
            "service_fee": "40.00",
            "status_client": "Terminé",
            "status_supplier": "Terminé",
        }

        res = self.client.patch(
            detail_url_prestation(client.id), payload, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["offer_price"], payload["offer_price"])
        self.assertEqual(res.data["status_client"], payload["status_client"])

    def test_full_update_client(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )
        client2 = Client.objects.create(
            first_name="John2", last_name="Doe2", email="johndoe2@gmail.com"
        )
        supplier = Supplier.objects.create(
            first_name="David",
            last_name="Mvoula2",
            email="davidmvoula@gmail.com",
            company_name="Mvoula Inc",
        )
        supplier2 = Supplier.objects.create(
            first_name="David",
            last_name="Mvoula",
            email="davidmvoula2@gmail.com",
            company_name="Mvoula Inc",
        )

        prestation = Prestation.objects.create(
            client=client,
            supplier=supplier,
            offer_price="100.00",
            service_fee="20.00",
            status_client="Action requise",
            status_supplier="Action requise",
            type_prestation="Informatique",
            charge_id="12",
            refund_id="34",
            charge_capture=False,
        )

        payload = {
            "offer_price": "200.00",
            "service_fee": "40.00",
            "status_client": "Terminé",
            "status_supplier": "Terminé",
            "type_prestation": "Immobilière",
            "charge_id": "123",
            "refund_id": "343",
            "charge_capture": False,
            "client": client2.id,
            "supplier": supplier2.id,
        }
        res = self.client.put(
            detail_url_prestation(prestation.id), payload, format="json"
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(client2.id, res.data["client"])
        self.assertEqual(supplier2.id, res.data["supplier"])
