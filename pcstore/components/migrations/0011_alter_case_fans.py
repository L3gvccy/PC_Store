# Generated by Django 5.2 on 2025-04-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0010_alter_psu_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='fans',
            field=models.IntegerField(),
        ),
    ]
