# Generated by Django 2.2.4 on 2019-09-26 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('potshop', '0015_auto_20190926_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]