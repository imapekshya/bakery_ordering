# Generated by Django 4.0.4 on 2022-05-17 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0013_remove_branch_id_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('C', 'Cake'), ('B', 'Bread'), ('CK', 'Cookies')], max_length=2),
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
