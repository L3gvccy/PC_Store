from django.db import models
from django.contrib.auth.models import User

class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('components.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Замовлення #{self.order.pk} від {self.order.user.username}: {self.product.display_name} x {self.quantity}"


class Order(models.Model):
    DELIVERY_CHOICES = [
        ('store_pickup', 'Самовивіз із наших магазинів'),
        ('courier', 'Кур’єр на вашу адресу'),
        ('post_office', 'Самовивіз з пошти'),
    ]
    
    POST_COMPANIES = [
        ('nova_poshta', 'Нова пошта'),
        ('meest', 'Meest'),
        ('ukrposhta', 'Укр пошта'),
    ]

    STATUS_CHOICES = [
        ('Очікує', 'Очікує'),
        ('Опрацьовується', 'Опрацьовується'),
        ('Відправлено', 'Відправлено'),
        ('Доставлено', 'Доставлено'),
        ('Скасовано', 'Скасовано'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
=======
>>>>>>> c4c30a5 (Add order)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_type = models.CharField(max_length=50, choices=DELIVERY_CHOICES)
    post_company = models.CharField(max_length=50, choices=POST_COMPANIES, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Очікує", verbose_name="Order status")
<<<<<<< HEAD
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
=======
>>>>>>> c4c30a5 (Add order)

    def __str__(self):
        return f"Замовлення #{self.pk} від {self.user.username}"
