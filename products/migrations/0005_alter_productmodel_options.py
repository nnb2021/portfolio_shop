# Generated by Django 4.0.4 on 2022-06-01 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productmodel_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
