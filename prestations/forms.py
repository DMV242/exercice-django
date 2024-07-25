from django import forms
from .models import Prestation


# Formulaire pour créer et mettre à jour une prestation
# TODO: Créez un formulaire pour créer et mettre à jour une prestation
class PrestationForm(forms.ModelForm):
    class Meta:
        model = Prestation
        fields = "__all__"
        exclude = ["charge_id", "refund_id"]
        widgets = {
            "client": forms.Select(attrs={"class": "form-control"}),
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "offer_price": forms.NumberInput(attrs={"class": "form-control"}),
            "service_fee": forms.NumberInput(attrs={"class": "form-control"}),
            "status_client": forms.Select(attrs={"class": "form-control"}),
            "status_supplier": forms.Select(attrs={"class": "form-control"}),
            "type_prestation": forms.TextInput(attrs={"class": "form-control"}),
        }
