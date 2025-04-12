from django.urls import path
from . import views

urlpatterns = [
    path('cpus/', views.CPUs_view),
    path('cpu_detail/<int:cpu_id>/', views.cpu_detail, name='cpu_detail'),
    path('motherboards/', views.Motherboards_view),
    path('motherboard_detail/<int:motherboard_id>/', views.motherboard_detail, name='motherboard_detail'),
]
