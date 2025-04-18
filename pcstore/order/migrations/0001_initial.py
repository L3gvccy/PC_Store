# Generated by Django 5.2 on 2025-04-13 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_type', models.CharField(choices=[('store_pickup', 'Самовивіз із наших магазинів'), ('courier', 'Кур’єр на вашу адресу'), ('post_office', 'Самовивіз з пошти')], max_length=50)),
                ('post_company', models.CharField(blank=True, choices=[('nova_poshta', 'Нова пошта'), ('meest', 'Meest'), ('ukrposhta', 'Укр пошта')], max_length=50, null=True)),
                ('status', models.CharField(default='Очікує', max_length=20, verbose_name='Статус замовлення')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
