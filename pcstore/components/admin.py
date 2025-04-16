from django.contrib import admin
from .models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case

# Register your models here.
admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(Storage)
admin.site.register(PSU)
admin.site.register(Cooler)
admin.site.register(AIO)
admin.site.register(Case)