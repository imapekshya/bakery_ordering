# Generated by Django 4.0.4 on 2022-05-14 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0009_remove_cart_product_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discounted_price',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.PositiveIntegerField(default=1)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bakery.product')),
            ],
        ),
    ]
