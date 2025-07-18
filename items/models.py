from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    seller = models.ForeignKey(User , on_delete= models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name}'
    

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return f'{self.item.name} Item'    
    

class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.item.name} -{self.quantity}'