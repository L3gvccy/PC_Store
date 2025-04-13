from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('my_orders/', views.view_orders, name='my_orders'),
=======
>>>>>>> c4c30a5 (Add order)
=======
    path('my_orders/', views.view_orders, name='my_orders'),
>>>>>>> 0045f6f (add my_orders)
]
