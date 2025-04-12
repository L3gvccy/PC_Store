from django.contrib import admin
from .models import CPU, Motherboard, GPU, RAM

# Register your models here.
admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(GPU)
admin.site.register(RAM)