# Generated by Django 4.0.4 on 2022-05-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0014_alter_product_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
