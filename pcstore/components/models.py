from django.db import models

# Create your models here.

class CPU(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=25)
    socket = models.CharField(max_length=25)
    cores = models.IntegerField()
    threads = models.IntegerField()
    frequency = models.FloatField(help_text="GHz")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name