# Generated by Django 4.0.4 on 2022-05-14 08:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0007_remove_payment_product_payment_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('quantity', models.PositiveIntegerField(default=1)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bakery.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery.product')),
            ],
        ),
    ]
