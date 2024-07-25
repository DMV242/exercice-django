from django.contrib import admin
from .models import Client, Supplier, Prestation
from django.utils.translation import gettext_lazy as _


class clientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("first_name", "last_name", "email")
    ordering = ("first_name", "last_name", "email")


class supplierAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "company_name")
    search_fields = ("first_name", "last_name", "email", "company_name")
    list_filter = ("first_name", "last_name", "email", "company_name")
    ordering = ("first_name", "last_name", "email", "company_name")


class PrestationAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "supplier",
        "offer_price",
        "service_fee",
        "status_client",
        "status_supplier",
        "type_prestation",
        "charge_id",
        "refund_id",
        "charge_capture",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "client__first_name",
        "client__last_name",
        "supplier__first_name",
        "supplier__last_name",
        "offer_price",
        "service_fee",
        "status_client",
        "status_supplier",
        "type_prestation",
        "charge_id",
        "refund_id",
        "charge_capture",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "client",
        "supplier",
        "offer_price",
        "service_fee",
        "status_client",
        "status_supplier",
        "type_prestation",
        "charge_id",
        "refund_id",
        "charge_capture",
        "created_at",
        "updated_at",
    )
    ordering = (
        "client",
        "supplier",
        "offer_price",
        "service_fee",
        "status_client",
        "status_supplier",
        "type_prestation",
        "charge_id",
        "refund_id",
        "charge_capture",
        "created_at",
        "updated_at",
    )


admin.site.register(Client, clientAdmin)
admin.site.register(Supplier, supplierAdmin)
admin.site.register(Prestation, PrestationAdmin)


admin.site.site_header = _("Espace d'administration des prestations")
admin.site.index_title = _(
    "Bienvenue dans l'interface d'administration des prestations"
)
