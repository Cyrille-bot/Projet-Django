from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits")
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    adresse = models.TextField()

    def __str__(self):
        return self.nom


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    adresse = models.TextField()

    def __str__(self):
        return self.nom


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commande {self.id} - {self.client.nom}"


class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_disponible = models.IntegerField()
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite_disponible} en stock"
