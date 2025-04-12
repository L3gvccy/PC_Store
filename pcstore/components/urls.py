from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.components),
    path('cpus/', views.CPUs_view, name='cpus'),
    path('cpu_detail/<int:cpu_id>/', views.cpu_detail, name='cpu_detail'),
<<<<<<< HEAD
    path('motherboards/', views.Motherboards_view, name='motherboards'),
    path('motherboard_detail/<int:motherboard_id>/', views.motherboard_detail, name='motherboard_detail'),
    path('gpus/', views.GPUs_view, name='gpus'),
    path('gpu_detail/<int:gpu_id>/', views.gpu_detail, name='gpu_detail'),
    path('rams/', views.RAMs_view, name='rams'),
    path('ram_detail/<int:ram_id>/', views.ram_detail, name='ram_detail'),
    path('storages/', views.Storages_view, name='storages'),
    path('storage_detail/<int:storage_id>/', views.storage_detail, name='storage_detail'),
    path('psus/', views.PSUs_view, name='psus'),
    path('psu_detail/<int:psu_id>/', views.psu_detail, name='psu_detail'),
    path('coolers/', views.Coolers_view, name='coolers'),
    path('cooler_detail/<int:cooler_id>/', views.cooler_detail, name='cooler_detail'),
    path('aios/', views.AIOs_view, name='aios'),
    path('aio_detail/<int:aio_id>/', views.aio_detail, name='aio_detail'),
    path('cases/', views.Cases_view, name='cases'),
    path('case_detail/<int:case_id>/', views.case_detail, name='case_detail'),
=======
    path('cpus/', views.CPUs_view),
<<<<<<< HEAD
>>>>>>> ec58bea (add cpus page)
=======
    path('cpu_detail/<int:cpu_id>/', views.cpu_detail, name='cpu_detail'),
>>>>>>> 31afb41 (update cart, add cpu detail, add cart item cout)
=======
    path('motherboards/', views.Motherboards_view),
<<<<<<< HEAD
>>>>>>> 3cce6bf (add motherboards)
=======
    path('motherboard_detail/<int:motherboard_id>/', views.motherboard_detail, name='motherboard_detail'),
>>>>>>> 246302b (add motherboard details)
]
