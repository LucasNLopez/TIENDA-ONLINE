# Generated by Django 4.1 on 2022-09-05 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=100),
        ),
    ]
