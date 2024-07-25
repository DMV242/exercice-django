from django.urls import reverse


PRESTATION_URL = reverse("prestation-list")
CLIENT_URL = reverse("client-list")
SUPPLIER_URL = reverse("supplier-list")


def detail_url_prestation(prestation_id):
    return reverse("prestation-detail", kwargs={"pk": prestation_id})


def detail_url_client(prestation_id):
    return reverse("client-detail", kwargs={"pk": prestation_id})


def detail_url_supplier(prestation_id):
    return reverse("supplier-detail", kwargs={"pk": prestation_id})
