from django.test import TestCase
from ..models import Prestation, Client, Supplier


class TestPrestationModel(TestCase):

    def setUp(self):
        pass

    def test_create_prestation(self):

        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )
        supplier = Supplier.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="janedoe@gmail.com",
            company_name="Doe Inc",
        )

        prestation = Prestation.objects.create(
            client=client,
            supplier=supplier,
            offer_price=1000,
            service_fee=200,
            status_client="Action requise",
            status_supplier="Action requise",
            type_prestation="Type prestation",
            charge_id="ch_1",
            refund_id="re_1",
        )

        self.assertEqual(prestation.client.id, client.id)
        self.assertEqual(prestation.supplier.id, supplier.id)


class TestClientModel(TestCase):

    def setUp(self):
        pass

    def test_create_client(self):
        client = Client.objects.create(
            first_name="John", last_name="Doe", email="johndoe@gmail.com"
        )
        self.assertEqual(client.first_name, "John")
        self.assertEqual(client.last_name, "Doe")
        self.assertEqual(client.email, "johndoe@gmail.com")


class TestSupplierModel(TestCase):

    def setUp(self):
        pass

    def test_create_supplier(self):
        supplier = Supplier.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="janedoe@gmail",
            company_name="Doe Inc",
        )

        self.assertEqual(supplier.first_name, "Jane")
        self.assertEqual(supplier.last_name, "Doe")
        self.assertEqual(supplier.email, "janedoe@gmail")
        self.assertEqual(supplier.company_name, "Doe Inc")
