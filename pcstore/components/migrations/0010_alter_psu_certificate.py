# Generated by Django 5.2 on 2025-04-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0009_aio_case_cooler_psu_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psu',
            name='certificate',
            field=models.CharField(choices=[('80 Plus Titanium', '80 Plus Titanium'), ('80 Plus Platinum', '80 Plus Platinum'), ('80 Plus Gold', '80 Plus Gold'), ('80 Plus Silver', '80 Plus Silver'), ('80 Plus Bronze', '80 Plus Bronze'), ('Без сертифікату', 'Без сертифікату')], default='Без сертифікату', max_length=25),
        ),
    ]
