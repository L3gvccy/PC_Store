from django.db import models
from django.apps import apps

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

class CPU(Product):
    brand = models.CharField(max_length=25)
    socket = models.CharField(max_length=25)
    cores = models.IntegerField()
    threads = models.IntegerField()
    frequency = models.FloatField(help_text="GHz")
    TDP = models.IntegerField(help_text="Watt", default=0)

class Motherboard(Product):
    brand = models.CharField(max_length=25)
    socket = models.CharField(max_length=25)
    chipset = models.CharField(max_length=25)
    form_factor = models.CharField(max_length=25, default="ATX")
    RAM_slots = models.IntegerField()
    RAM_type = models.CharField(max_length=25)
    M2_slots = models.IntegerField()
    WiFi = models.BooleanField(default=False)
    Bluetooth = models.BooleanField(default=False)

class GPU(Product):
    brand = models.CharField(max_length=25)
    gp_brand = models.CharField(max_length=25)
    series = models.CharField(max_length=25)
    memory = models.IntegerField(help_text="GB")
    memory_type = models.CharField(max_length=25)
    TDP = models.IntegerField(help_text="Watt", default=0)

class RAM(Product):
    brand = models.CharField(max_length=25)
    capacity = models.IntegerField(help_text="GB")
    ram_type = models.CharField(max_length=25)
    frequency = models.IntegerField(help_text="MHz")
    number_of_modules = models.IntegerField(default=1)
