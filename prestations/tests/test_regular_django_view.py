from django.test import TestCase, Client as ClientDjango
from django.urls import reverse


class IntregationTestPrestation(TestCase):

    def setUp(self):
        self.client = ClientDjango()

    def test_view_response_status_code(self):
        response = self.client.get(reverse("list_prestation"))
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        response = self.client.get(reverse("list_prestation"))
        self.assertTemplateUsed(response, "prestations/prestation_list.html")

    def test_view_context_data(self):
        response = self.client.get(reverse("list_prestation"))
        self.assertIn("prestations", response.context)
