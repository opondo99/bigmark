# Generated by Django 2.2.4 on 2019-09-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potshop', '0002_product_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
