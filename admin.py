from django.contrib import admin
from .models import Produit, Categorie, Client, Fournisseur, Commande, Stock

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Commande)
admin.site.register(Stock)
