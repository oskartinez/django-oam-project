# Generated by Django 4.1 on 2022-09-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_alter_articulo_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='domicilio',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
