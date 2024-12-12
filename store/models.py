from django.db import models
from django.urls import reverse

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