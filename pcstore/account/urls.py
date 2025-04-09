from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout),
    path('register/', views.register_user),
]
