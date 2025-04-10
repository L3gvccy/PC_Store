from django.urls import path
from . import views

urlpatterns = [
    path('cpus/', views.CPUs_view),
]
