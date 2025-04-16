from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
=======
    path('add/<int:cpu_id>/', views.add_to_cart, name='add_to_cart'),
=======
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
>>>>>>> f236aa0 (update cart)
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
>>>>>>> 4efcee2 (Add cart)
]
