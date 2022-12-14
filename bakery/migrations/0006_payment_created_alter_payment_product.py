# Generated by Django 4.0.4 on 2022-05-14 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0005_payment_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bakery.product'),
        ),
    ]
