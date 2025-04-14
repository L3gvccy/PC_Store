from django.urls import path
from . import views


urlpatterns = [
    path('', views.configurator_view, name="configurator"),
    path('select_cpu/<int:cpu_id>/', views.select_cpu, name="select_cpu"),
]
