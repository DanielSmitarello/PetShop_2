# Generated by Django 4.0.4 on 2022-07-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0005_alter_productos_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('promo_img', models.ImageField(blank=True, null=True, upload_to='promo_image')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
        ),
    ]