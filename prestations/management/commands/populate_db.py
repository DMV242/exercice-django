import random
from django.core.management.base import BaseCommand
from faker import Faker
from prestations.models import Client, Supplier, Prestation


class Command(BaseCommand):
    help = "Populate the database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        clients = []
        for _ in range(10):
            client = Client(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
            )
            client.save()
            clients.append(client)

        suppliers = []
        for _ in range(10):
            supplier = Supplier(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                company_name=fake.company(),
            )
            supplier.save()
            suppliers.append(supplier)

        status_choices = [
            "Action requise",
            "Attendre",
            "Terminé",
            "Annulé",
            "Confirme",
            "En attente",
            "Waiting Approval",
        ]

        for _ in range(20):
            prestation = Prestation(
                client=random.choice(clients),
                supplier=random.choice(suppliers),
                offer_price=fake.random_number(digits=5),
                service_fee=fake.random_number(digits=3),
                status_client=random.choice(status_choices),
                status_supplier=random.choice(status_choices),
                type_prestation=fake.word(),
                charge_id=fake.unique.uuid4(),
                refund_id=fake.unique.uuid4(),
                charge_capture=fake.boolean(),
            )
            prestation.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with fake data.")
        )
