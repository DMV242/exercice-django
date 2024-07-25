from rest_framework import serializers
from .models import Prestation, Client, Supplier
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class PrestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestation
        fields = "__all__"
        read_only_fields = ["id"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ["id"]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        read_only_fields = ["id"]
