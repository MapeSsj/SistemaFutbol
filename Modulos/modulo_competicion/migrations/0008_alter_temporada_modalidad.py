# Generated by Django 4.2.4 on 2023-10-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_competicion', '0007_formato_posicion_repesca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporada',
            name='modalidad',
            field=models.CharField(choices=[('EUROPEA', 'EUROPEA'), ('LIGA', 'LIGA'), ('Copa de Europa (UEFA Champions League)', 'Copa de Europa (UEFA Champions League)'), ('TORNEO', 'TORNEO'), ('COPA PAIS', 'COPA PAIS'), ('SELECCIONES', 'SELECCIONES')], max_length=100),
        ),
    ]
