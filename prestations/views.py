from django.urls import reverse_lazy
from .models import Client, Supplier, Prestation
from rest_framework import viewsets
from prestations.serializers import (
    PrestationSerializer,
    ClientSerializer,
    SupplierSerializer,
)


from prestations.permissions import IsAuthenticatedOrReadOnly
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from prestations.forms import PrestationForm


# Vue pour lister toutes les prestations
# TODO: Créez une vue pour lister toutes les prestations
class ListPrestation(ListView):
    model = Prestation
    template_name = "prestations/list_prestation.html"
    context_object_name = "prestations"
    ordering = ["-created_at"]
    paginate_by = 10


# Vue pour afficher les détails d'une prestation spécifique
# TODO: Créez une vue pour afficher les détails d'une prestation spécifique
class DetailPrestation(DetailView):
    model = Prestation
    template_name = "prestations/prestation_detail.html"
    context_object_name = "prestation"
    pk_url_kwarg = "prestation_id"


# Vue pour créer une nouvelle prestation
# TODO: Créez une vue pour créer une nouvelle prestation


class CreatePresation(CreateView):
    model = Prestation
    template_name = "prestations/prestation_form.html"
    form_class = PrestationForm
    success_url = reverse_lazy("list_prestation")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        return context


# Vue pour mettre à jour une prestation existante
# TODO: Créez une vue pour mettre à jour une prestation existante


class UpdatePrestation(UpdateView):
    model = Prestation
    template_name = "prestations/prestation_form.html"
    form_class = PrestationForm
    pk_url_kwarg = "prestation_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context

    def get_success_url(self):
        return reverse_lazy(
            "detail_prestation", kwargs={"prestation_id": self.object.id}
        )


# Vue pour supprimer une prestation existante
# TODO: Créez une vue pour supprimer une prestation existante
class DeletePrestation(DeleteView):
    model = Prestation
    template_name = "prestations/prestation_confirm_delete.html"
    success_url = reverse_lazy("list_prestation")
    pk_url_kwarg = "prestation_id"


# Vue pour les clients
class ListClient(ListView):
    model = Client
    template_name = "clients/list_client.html"
    context_object_name = "clients"


# API VIEWS
class PrestationViewSet(viewsets.ModelViewSet):
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SupplierModelViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
