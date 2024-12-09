from django.db import models

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
    # le champ pour le nom, c'est la  longuer du nom
    name = models.CharField(max_length=128)
    # Pour le prix de l'article
    price = models.FloatField(default=0.0)
    # Pour la quantite en stok
    stok = models.FloatField(default=0)
    # pourquoi textfield ? Juste par ce qu'il prend plus de carataire que le charfield
    description = models.TextField(blank=True)
    #Pour cree une image
    image = models.ImageField(upload_to = 'products', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stok})"
