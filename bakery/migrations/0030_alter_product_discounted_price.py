# Generated by Django 4.0.4 on 2022-07-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0029_product_discounted_price_alter_product_selling_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
