# Generated by Django 4.0.4 on 2022-05-19 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0018_product_flavour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='flavour',
        ),
    ]
