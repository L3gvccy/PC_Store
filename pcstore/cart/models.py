from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('components.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product') 

<<<<<<< HEAD
<<<<<<< HEAD
=======
    def __str__(self):
        return f"{self.cpu.name} x{self.quantity} для {self.user.username}"
>>>>>>> 4efcee2 (Add cart)
=======
>>>>>>> 3cce6bf (add motherboards)
