# Generated by Django 4.1 on 2022-09-09 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_proveedor_domicilio_proveedor_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='domicilio',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
