from django.db import models
from django.contrib.auth.models import User
from components.models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case

# Create your models here.
class Configuration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.SET_NULL, null=True, blank=True)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, null=True, blank=True)
    gpu = models.ForeignKey(GPU, on_delete=models.SET_NULL, null=True, blank=True)
    ram = models.ForeignKey(RAM, on_delete=models.SET_NULL, null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.SET_NULL, null=True, blank=True)
    psu = models.ForeignKey(PSU, on_delete=models.SET_NULL, null=True, blank=True)
    cooler = models.ForeignKey(Cooler, on_delete=models.SET_NULL, null=True, blank=True)
    aio = models.ForeignKey(AIO, on_delete=models.SET_NULL, null=True, blank=True)
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    