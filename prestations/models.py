from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Supplier(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Prestation(models.Model):
    Waiting_Approval = 'Waiting Approval'
    ActionRequired = 'Action requise'
    Waiting = 'Attendre'
    Client_Wait = 'En attente'
    Completed = 'Terminé'
    Cancelled = 'Annulé'
    Confirmed = 'Confirmé'

    STATUS_CHOICES = (
        (ActionRequired, 'Action requise'),
        (Waiting, 'Attendre'),
        (Completed, 'Terminé'),
        (Cancelled, 'Annulé'),
        (Confirmed, 'Confirme'),
        (Client_Wait, 'En attente'),
        (Waiting_Approval, 'Waiting Approval'),
    )

    client = models.ForeignKey(Client, related_name='supplier_offer', on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, related_name='supplier_offer', on_delete=models.PROTECT)

    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_fee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    status_client = models.CharField(max_length=20, choices=STATUS_CHOICES, default=Client_Wait)
    status_supplier = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ActionRequired)

    type_prestation = models.CharField(max_length=35, null=True, blank=True)

    charge_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
    refund_id = models.CharField(max_length=255, null=True, blank=True, unique=True)

    charge_capture = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def supplier_name(self):
        return self.supplier.first_name + ' ' + self.supplier.last_name

    @property
    def client_name(self):
        return self.client.first_name + ' ' + self.client.last_name
