# Generated by Django 4.1 on 2022-09-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_alter_articulo_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]