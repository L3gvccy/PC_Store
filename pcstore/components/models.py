from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cce6bf (add motherboards)
from django.apps import apps

# Create your models here.
<<<<<<< HEAD
<<<<<<< HEAD
class Product(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

class CPU(Product):
=======

class CPU(models.Model):
    name = models.CharField(max_length=255)
>>>>>>> ec58bea (add cpus page)
=======
class Product(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.display_name

class CPU(Product):
>>>>>>> 98f1f15 (change cpu model)
    brand = models.CharField(max_length=25)
    socket = models.CharField(max_length=25)
    cores = models.IntegerField()
    threads = models.IntegerField()
    frequency = models.FloatField(help_text="GHz")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cce6bf (add motherboards)
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 01cc471 (Add GPU)

class GPU(Product):
    brand = models.CharField(max_length=25)
    gp_brand = models.CharField(max_length=25)
    series = models.CharField(max_length=25)
    memory = models.IntegerField(help_text="GB")
    memory_type = models.CharField(max_length=25)
    TDP = models.IntegerField(help_text="Watt", default=0)
<<<<<<< HEAD

class RAM(Product):
    brand = models.CharField(max_length=25)
    capacity = models.IntegerField(help_text="GB")
    ram_type = models.CharField(max_length=25)
    frequency = models.IntegerField(help_text="MHz")
    number_of_modules = models.IntegerField(default=1)

class Storage(Product):
    brand = models.CharField(max_length=25)
    capacity = models.CharField(max_length=25)
    storage_type = models.CharField(max_length=25)
    speed = models.IntegerField(help_text="MB/s")

class PSU(Product):
    certificate_choices = [
        ('80 Plus Titanium', '80 Plus Titanium'),
        ('80 Plus Platinum', '80 Plus Platinum'),
        ('80 Plus Gold', '80 Plus Gold'),
        ('80 Plus Silver', '80 Plus Silver'),
        ('80 Plus Bronze', '80 Plus Bronze'),
        ('Без сертифікату', 'Без сертифікату'),
    ]
    brand = models.CharField(max_length=25)
    series = models.CharField(max_length=50)
    wattage = models.IntegerField(help_text="Watt")
    certificate = models.CharField(max_length=25, choices=certificate_choices, default='Без сертифікату')
    modular = models.BooleanField(default=False)

class Cooler(Product):
    brand = models.CharField(max_length=25)
    heat_tube_number = models.IntegerField()
    height = models.IntegerField(help_text="mm")
    argb = models.BooleanField(default=False)
    max_tdp = models.IntegerField(help_text="Watt")

class AIO(Product):
    brand = models.CharField(max_length=25)
    size = models.IntegerField(help_text="mm")
    argb = models.BooleanField(default=False)
    max_tdp = models.IntegerField(help_text="Watt")

class Case(Product):
    brand = models.CharField(max_length=25)
    form_factor = models.CharField(max_length=25, default="ATX")
    fans = models.IntegerField()
    max_cooler_height = models.IntegerField(help_text="mm")
    max_aio_size = models.IntegerField(help_text="mm")
    tempered_glass = models.BooleanField(default=False)
=======

# Create your models here.
>>>>>>> 67d780e (add header)
=======
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
>>>>>>> ec58bea (add cpus page)
=======
    TDP = models.IntegerField(help_text="Watt", default=0)
>>>>>>> 98f1f15 (change cpu model)
=======
>>>>>>> 3cce6bf (add motherboards)
=======
>>>>>>> 01cc471 (Add GPU)
