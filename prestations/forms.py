from django import forms
from .models import Prestation
from django.utils.translation import gettext_lazy as _


# Formulaire pour créer et mettre à jour une prestation
# TODO: Créez un formulaire pour créer et mettre à jour une prestation
class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = "__all__"
        exclude = ["charge_id", "refund_id"]
        labels = {
            "client": _("Client"),
            "supplier": _("Fournisseur"),
            "offer_price": _("Prix de l'offre"),
            "service_fee": _("Frais de service"),
            "status_client": _("Statut client"),
            "status_supplier": _("Statut fournisseur"),
            "type_prestation": _("Type de prestation"),
            "charge_capture": _("Capture de charge"),
        }
        widgets = {
            "client": forms.Select(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mt-2 mb-4"
                }
            ),
            "supplier": forms.Select(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md  mt-2 mb-4",
                },
            ),
            "offer_price": forms.NumberInput(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md  mt-2 mb-4"
                }
            ),
            "service_fee": forms.NumberInput(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md  mt-2 mb-4"
                }
            ),
            "status_client": forms.Select(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md  mt-2 mb-4"
                }
            ),
            "status_supplier": forms.Select(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md  mt-2 mb-4"
                }
            ),
            "type_prestation": forms.TextInput(
                attrs={
                    "class": "w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md  mt-2 mb-4"
                }
            ),
        }
