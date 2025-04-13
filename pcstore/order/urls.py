from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('my_orders/', views.view_orders, name='my_orders'),
]
