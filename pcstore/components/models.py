from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CPU(Product):
    brand = models.CharField(max_length=25)
    socket = models.CharField(max_length=25)
    cores = models.IntegerField()
    threads = models.IntegerField()
    frequency = models.FloatField(help_text="GHz")
    TDP = models.IntegerField(help_text="Watt", default=0)