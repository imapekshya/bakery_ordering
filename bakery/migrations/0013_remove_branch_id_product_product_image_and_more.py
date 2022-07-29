# Generated by Django 4.0.4 on 2022-05-16 03:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0012_branch_product_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='1', upload_to='productimg'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
    ]
