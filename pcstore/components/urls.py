from django.urls import path
from . import views

urlpatterns = [
    path('', views.components),
    path('cpus/', views.CPUs_view),
    path('cpu_detail/<int:cpu_id>/', views.cpu_detail, name='cpu_detail'),
    path('motherboards/', views.Motherboards_view),
    path('motherboard_detail/<int:motherboard_id>/', views.motherboard_detail, name='motherboard_detail'),
    path('gpus/', views.GPUs_view),
    path('gpu_detail/<int:gpu_id>/', views.gpu_detail, name='gpu_detail'),
    path('rams/', views.RAMs_view),
    path('ram_detail/<int:ram_id>/', views.ram_detail, name='ram_detail'),
    path('storages/', views.Storages_view),
    path('storage_detail/<int:storage_id>/', views.storage_detail, name='storage_detail'),
    path('coolers/', views.Coolers_view),
    path('cooler_detail/<int:cooler_id>/', views.cooler_detail, name='cooler_detail'),
    path('aios/', views.AIOSs_view),
    path('aio_detail/<int:aio_id>/', views.aio_detail, name='aio_detail'),
]
