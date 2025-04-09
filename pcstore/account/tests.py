<<<<<<< HEAD
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AccountViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='oldpassword',
            email='test@example.com',
            first_name='Test',
            last_name='User'
        )

    def test_register_user_success(self):
        response = self.client.post(reverse('register_user'), {
            'username': 'newuser',
            'password': 'pass1234',
            'confirm_password': 'pass1234',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'new@example.com'
        })
        self.assertRedirects(response, '/account/login/')
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_user_success(self):
        response = self.client.post(reverse('login_user'), {
            'username': 'testuser',
            'password': 'oldpassword'
        })
        self.assertRedirects(response, '/')

    def test_login_user_invalid(self):
        response = self.client.post(reverse('login_user'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Невірне ім’я користувача або пароль.")

    def test_logout(self):
        self.client.login(username='testuser', password='oldpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/')

    def test_profile_user_update(self):
        self.client.login(username='testuser', password='oldpassword')
        response = self.client.post(reverse('profile_user'), {
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'updated@example.com'
        })
        self.assertRedirects(response, '/account/profile/')
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')

    def test_change_password_success(self):
        self.client.login(username='testuser', password='oldpassword')
        response = self.client.post(reverse('change_password'), {
            'old_password': 'oldpassword',
            'new_password': 'newsecurepassword',
            'confirm_password': 'newsecurepassword'
        })
        self.assertRedirects(response, '/account/profile/')
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newsecurepassword'))

    def test_change_password_mismatch(self):
        self.client.login(username='testuser', password='oldpassword')
        response = self.client.post(reverse('change_password'), {
            'old_password': 'oldpassword',
            'new_password': 'newpassword1',
            'confirm_password': 'newpassword2'
        })
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('oldpassword'))
=======
from django.test import TestCase

# Create your tests here.
>>>>>>> 0c2974f (Add registration)
