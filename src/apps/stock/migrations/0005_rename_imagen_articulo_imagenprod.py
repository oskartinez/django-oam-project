# Generated by Django 4.1 on 2022-08-26 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_articulo_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='imagen',
            new_name='imagenprod',
        ),
    ]
