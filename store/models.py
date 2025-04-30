from django.db import models
from django.db.models import OneToOneField, ManyToManyField
from django.urls import reverse

from shop.settings import AUTH_USER_MODEL

# Create your models here.

"""
Produit 
- Nom
- Prix 
- Quantite en stoks
- Discription
- Image
"""

class Product(models.Model) :

    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)

    stok = models.FloatField(default=0)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to = 'products', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stok})"

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


# Article (Order)
"""
- Utilisateur
- Produits 
- Commander ou non
"""
class Order(models.Model) :
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__ (self) :
        return f"{self.product.name} ({self.quantity})"

# Panier (Card)
"""
- Utilisateur 
- Articles
- Commander ou non
- Date de la commande
"""
class Cart(models.Model) :
    # oOn veut que l'utilisateur n'est qu'un seul panier
    user = OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) :
        return self.user.username
