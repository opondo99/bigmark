# Generated by Django 2.2.4 on 2019-10-09 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potshop', '0020_order_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='countries',
            new_name='country',
        ),
    ]
