from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name="Логін")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    first_name = models.CharField(max_length=100, verbose_name="Ім’я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище") 
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
