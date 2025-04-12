from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from .models import CPU, Motherboard, GPU, RAM, Storage, PSU, Cooler, AIO, Case
=======
from .models import CPU, Motherboard, GPU, RAM
>>>>>>> ef1f7ff (Add RAM)

# Register your models here.
admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(GPU)
<<<<<<< HEAD
admin.site.register(RAM)
admin.site.register(Storage)
admin.site.register(PSU)
admin.site.register(Cooler)
admin.site.register(AIO)
admin.site.register(Case)
=======

# Register your models here.
>>>>>>> 67d780e (add header)
=======
from .models import CPU

# Register your models here.
admin.site.register(CPU)
>>>>>>> ec58bea (add cpus page)
=======
from .models import CPU, Motherboard
=======
from .models import CPU, Motherboard, GPU
>>>>>>> f3827ea (Update CPU)

# Register your models here.
admin.site.register(CPU)
admin.site.register(Motherboard)
<<<<<<< HEAD
>>>>>>> 3cce6bf (add motherboards)
=======
admin.site.register(GPU)
>>>>>>> f3827ea (Update CPU)
=======
admin.site.register(RAM)
>>>>>>> ef1f7ff (Add RAM)
