# Generated by Django 4.1 on 2022-08-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='descripcion',
            field=models.CharField(default='-', max_length=50),
        ),
    ]