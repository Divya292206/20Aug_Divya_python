from django.db import models
from restaurants.models import Restaurant, MenuItem
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    status_choices = [
        ('PENDING', 'Pending'),
        ('PREPARING', 'Preparing'),
        ('OUT_OF_DELIVERY', 'out_of_delivery'),
        ('DELIVERED', 'Delivered'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status_choices, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name='order_items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)