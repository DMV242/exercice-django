from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prestations.views import (
    ListPrestation,
    DetailPrestation,
    CreatePresation,
    UpdatePrestation,
    DeletePrestation,
    ListClient,
    PrestationViewSet,
    ClientModelViewSet,
    SupplierModelViewSet,
)

router = routers.DefaultRouter()

router.register("prestations", PrestationViewSet)
router.register("clients", ClientModelViewSet)
router.register("suppliers", SupplierModelViewSet)

client_urls = [
    path("clients/", ListClient.as_view(), name="list_client"),
]


urlpatterns = [
    path("", ListPrestation.as_view(), name="list_prestation"),
    path(
        "voir_prestation/<int:prestation_id>/",
        DetailPrestation.as_view(),
        name="detail_prestation",
    ),
    path(
        "creer_prestation/",
        CreatePresation.as_view(),
        name="create_prestation",
    ),
    path(
        "modifier_prestation/<int:prestation_id>/",
        UpdatePrestation.as_view(),
        name="update_prestation",
    ),
    path(
        "supprimer_prestation/<int:prestation_id>/",
        DeletePrestation.as_view(),
        name="delete_prestation",
    ),
    path("api/", include(router.urls)),
] + client_urls
