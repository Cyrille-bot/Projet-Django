from django.shortcuts import render
from .models import Produit, Categorie, Client, Fournisseur, Commande


def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'Shope_Manage/liste_produits.html', {'produits': produits})


def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'Shope_Manage/liste_categories.html', {'categories': categories})


def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'Shope_Manage/liste_clients.html', {'clients': clients})


def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'Shope_Manage/liste_fournisseurs.html', {'fournisseurs': fournisseurs})


def liste_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'Shope_Manage/liste_commandes.html', {'commandes': commandes})
