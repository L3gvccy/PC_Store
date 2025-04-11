from django.urls import path
from . import views

urlpatterns = [
    path('cpus/', views.CPUs_view),
    path('cpu_detail/<int:cpu_id>/', views.cpu_detail, name='cpu_detail'),
]
