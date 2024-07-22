from django.contrib import admin
from .models import Client, Supplier, Prestation

admin.site.register(Client)
admin.site.register(Supplier)
admin.site.register(Prestation)
