# Generated by Django 4.2.4 on 2023-10-31 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_contrato', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(blank=True, default='jugador/jugador_default.png', null=True, upload_to='jugador/'),
        ),
    ]
