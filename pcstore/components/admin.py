from django.contrib import admin
from .models import CPU, Motherboard, GPU

# Register your models here.
admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(GPU)