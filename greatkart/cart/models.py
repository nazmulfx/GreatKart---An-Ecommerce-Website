from django.db import models

from store.models import Product
# Create your models here.
class Cart(models.Model):
    cartId = models.CharField(max_length=250, blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cartId
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product