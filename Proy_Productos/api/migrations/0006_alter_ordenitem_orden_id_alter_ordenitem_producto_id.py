# Generated by Django 4.2.7 on 2023-11-05 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_orden_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenitem',
            name='orden_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.orden'),
        ),
        migrations.AlterField(
            model_name='ordenitem',
            name='producto_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orden_items', to='api.productos'),
        ),
    ]