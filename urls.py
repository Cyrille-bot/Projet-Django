from django.urls import path
from .views import liste_produits, liste_categories, liste_clients, liste_fournisseurs, liste_commandes

urlpatterns = [
    path('produits/', liste_produits, name='liste_produits'),
    path('categories/', liste_categories, name='liste_categories'),
    path('clients/', liste_clients, name='liste_clients'),
    path('fournisseurs/', liste_fournisseurs, name='liste_fournisseurs'),
    path('commandes/', liste_commandes, name='liste_commandes'),
]
