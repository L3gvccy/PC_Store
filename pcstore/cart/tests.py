<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a0c7302 (Add tests for cart)
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from components.models import Product
from .models import CartItem
<<<<<<< HEAD

class CartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test product', price=100, quantity=10)

    def login(self):
        self.client.login(username='testuser', password='12345')

    def test_add_to_cart_authenticated(self):
        self.login()
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(CartItem.objects.count(), 1)
        cart_item = CartItem.objects.first()
        self.assertEqual(cart_item.quantity, 1)
        self.assertEqual(cart_item.product, self.product)

    def test_add_to_cart_not_authenticated(self):
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CartItem.objects.count(), 0)

    def test_increase_quantity(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get(reverse('increase_quantity', args=[item.id]))
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.quantity, 2)

    def test_increase_quantity_exceed_stock(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=self.product.quantity)
        response = self.client.get(reverse('increase_quantity', args=[item.id]))
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.quantity, self.product.quantity)

    def test_decrease_quantity_above_one(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)
        response = self.client.get(reverse('decrease_quantity', args=[item.id]))
        item.refresh_from_db()
        self.assertEqual(item.quantity, 1)

    def test_decrease_quantity_to_zero(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get(reverse('decrease_quantity', args=[item.id]))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_clear_cart(self):
        self.login()
        CartItem.objects.create(user=self.user, product=self.product, quantity=3)
        response = self.client.get(reverse('clear_cart'))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_remove_from_cart(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get(reverse('remove_from_cart', args=[item.id]))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_view_cart_not_authenticated(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 302)
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> 4efcee2 (Add cart)
=======

class CartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test product', price=100, quantity=10)

    def login(self):
        self.client.login(username='testuser', password='12345')

    def test_add_to_cart_authenticated(self):
        self.login()
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(CartItem.objects.count(), 1)
        cart_item = CartItem.objects.first()
        self.assertEqual(cart_item.quantity, 1)
        self.assertEqual(cart_item.product, self.product)

    def test_add_to_cart_not_authenticated(self):
        response = self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CartItem.objects.count(), 0)

    def test_increase_quantity(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get(reverse('increase_quantity', args=[item.id]))
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.quantity, 2)

    def test_increase_quantity_exceed_stock(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=self.product.quantity)
        response = self.client.get(reverse('increase_quantity', args=[item.id]))
        self.assertEqual(response.status_code, 302)
        item.refresh_from_db()
        self.assertEqual(item.quantity, self.product.quantity)

    def test_decrease_quantity_above_one(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)
        response = self.client.get(reverse('decrease_quantity', args=[item.id]))
        item.refresh_from_db()
        self.assertEqual(item.quantity, 1)

    def test_decrease_quantity_to_zero(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get(reverse('decrease_quantity', args=[item.id]))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_clear_cart(self):
        self.login()
        CartItem.objects.create(user=self.user, product=self.product, quantity=3)
        response = self.client.get(reverse('clear_cart'))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_remove_from_cart(self):
        self.login()
        item = CartItem.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get(reverse('remove_from_cart', args=[item.id]))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_view_cart_not_authenticated(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 302)
>>>>>>> a0c7302 (Add tests for cart)
