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
]
