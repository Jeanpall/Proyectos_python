# Generated by Django 4.2.7 on 2023-12-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_categorias_alter_productos_catproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenitem',
            name='total',
            field=models.DecimalField(auto_created=True, decimal_places=2, default=0, editable=False, max_digits=10),
        ),
    ]
