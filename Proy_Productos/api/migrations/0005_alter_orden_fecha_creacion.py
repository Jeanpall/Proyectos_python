# Generated by Django 4.2.7 on 2023-11-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
