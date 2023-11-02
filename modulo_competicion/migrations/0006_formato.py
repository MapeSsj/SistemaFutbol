# Generated by Django 4.2.6 on 2023-10-22 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_competicion', '0005_tipo_equipo_tipo_competicion'),
    ]

    operations = [
        migrations.CreateModel(
            name='formato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('cantidad_equipos', models.PositiveSmallIntegerField(default=1)),
                ('cantidad_grupos', models.PositiveSmallIntegerField(default=1)),
                ('tabla_acumulada', models.BooleanField(default=False)),
                ('cantidad_equipos_x_grupo', models.PositiveSmallIntegerField(default=1)),
                ('fase_apertura', models.BooleanField(default=False)),
                ('fase_clausura', models.BooleanField(default=False)),
                ('cantidad_jornadas', models.PositiveSmallIntegerField(default=1)),
                ('cantidad_equipos_clasificacion_directa', models.PositiveSmallIntegerField(default=1)),
                ('cantidad_equipos_clasificacion_grupo', models.PositiveSmallIntegerField(default=1)),
                ('play_off', models.BooleanField(default=False)),
                ('cantidad_equipos_clasificacion_fase_previa', models.PositiveSmallIntegerField(default=1)),
                ('cantidad_etapas', models.CharField(choices=[(6, '32avos de Final '), (5, '16avos de Final'), (4, '8avos de Final'), (3, '4tos de Final '), (2, 'Semifinal'), (1, 'Final')], max_length=2)),
                ('fase_grupos', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_competicion.temporada')),
                ('tipo_competicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_competicion.tipo_competicion')),
            ],
        ),
    ]
