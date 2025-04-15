from django.urls import path
from . import views


urlpatterns = [
    path('', views.configurator_view, name="configurator"),
    path('select_cpu/<int:cpu_id>/', views.select_cpu, name="select_cpu"),
    path('remove_cpu/', views.remove_cpu, name="remove_cpu"),
    path('select_mb/<int:mb_id>/', views.select_mb, name="select_mb"),
    path('remove_mb/', views.remove_mb, name="remove_mb"),
    path('select_ram/<int:ram_id>/', views.select_ram, name="select_ram"),
    path('remove_ram/', views.remove_ram, name="remove_ram"),
    path('select_gpu/<int:gpu_id>/', views.select_gpu, name="select_gpu"),
    path('remove_gpu/', views.remove_gpu, name="remove_gpu"),
    path('select_storage/<int:storage_id>/', views.select_storage, name="select_storage"),
    path('remove_storage/', views.remove_storage, name="remove_storage"),
    path('select_psu/<int:psu_id>/', views.select_psu, name="select_psu"),
    path('remove_psu/', views.remove_psu, name="remove_psu"),
    path('select_cooler/<int:cooler_id>/', views.select_cooler, name="select_cooler"),
    path('remove_cooler/', views.remove_cooler, name="remove_cooler"),
    path('select_aio/<int:aio_id>/', views.select_aio, name="select_aio"),
    path('remove_aio/', views.remove_aio, name="remove_aio"),
    path('select_case/<int:case_id>/', views.select_case, name="select_case"),
    path('remove_case/', views.remove_case, name="remove_case"),
    path('clear_configuration/', views.clear_configuration, name="clear_configuration"),
    path('err_configuration/', views.err_configuration, name="err_configuration"),
    path('save_configuration/', views.save_configuration, name="save_configuration"),
]
