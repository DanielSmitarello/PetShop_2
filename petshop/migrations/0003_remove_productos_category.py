# Generated by Django 4.0.4 on 2022-06-24 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0002_alter_productos_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='category',
        ),
    ]
