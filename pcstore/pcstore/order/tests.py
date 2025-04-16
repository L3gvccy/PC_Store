from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order, OrderItem
from cart.models import CartItem
from components.models import Product
from decimal import Decimal

class OrderModelTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.product = Product.objects.create(
            name='Test Product',
            price=50.00,
            quantity=10,
            display_name='Test Product Display'
        )
        self.order = Order.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone_number='1234567890',
            delivery_type='store_pickup',
            status='Очікує',
            total_price=100.00
        )
        self.cart_item = CartItem.objects.create(
            user=self.user,
            product=self.product,
            quantity=2
        )

    def test_order_creation_and_str(self):
        self.assertEqual(str(self.order), f"Замовлення #{self.order.pk} від {self.user.username}")
        self.assertEqual(self.order.status, 'Очікує')
        self.assertEqual(self.order.total_price, Decimal('100.00'))

    def test_order_item_creation_and_str(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )
        self.assertEqual(
            str(order_item),
            f"Замовлення #{self.order.pk} від {self.user.username}: {self.product.display_name} x 3"
        )
        self.assertEqual(order_item.quantity, 3)

    def test_checkout_view_get_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/checkout.html')
        self.assertEqual(response.context['total_price'], Decimal('100.00'))
        self.assertEqual(len(response.context['cart_items']), 1)

    def test_checkout_view_post_valid(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'phone_number': '0987654321',
            'delivery_type': 'courier'
        }
        response = self.client.post(reverse('checkout'), data)
        self.assertRedirects(response, reverse('order_success'))
        
        self.assertEqual(Order.objects.count(), 2) 
        new_order = Order.objects.last()
        self.assertEqual(new_order.total_price, Decimal('100.00'))
        
        self.product.refresh_from_db() 
        self.assertEqual(self.product.quantity, 8) 

        self.assertEqual(CartItem.objects.count(), 0)

    def test_checkout_view_empty_cart(self):
        self.client.login(username='testuser', password='testpass123')
        CartItem.objects.all().delete()
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, '/', status_code=302)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), "Додайте хочаб один товар, щоб створити замволення.")

    def test_order_success_view(self):
        response = self.client.get(reverse('order_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order_success.html')

    def test_view_orders_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('my_orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/my_orders.html')
        self.assertEqual(len(response.context['orders']), 1)
        self.assertEqual(response.context['orders'][0].pk, self.order.pk)

    def test_view_orders_unauthenticated(self):
        response = self.client.get(reverse('my_orders'))
        self.assertEqual(response.status_code, 302)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]), "Вам потрібно увійти в систему, щоб переглянути замовлення.")