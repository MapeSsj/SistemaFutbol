# Generated by Django 4.2.4 on 2023-10-30 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_competicion', '0017_jornada'),
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('norma', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'CIUDAD',
                'verbose_name_plural': 'CIUDADES',
            },
        ),
        migrations.CreateModel(
            name='sede',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('capacidad', models.PositiveSmallIntegerField(default=0)),
                ('fecha_inaguracion', models.DateField()),
                ('estado', models.CharField(choices=[('SD', 'SUSPENDIDO DEFINITIVAMENTE'), ('DI', 'DISPONIBLE'), ('EM', 'EN MANTENIMIENTO'), ('ND', 'NO DISPONIBLE'), ('ST', 'SUSPENDIDO TEMPORALMENTE')], max_length=2)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_encuentros.ciudad')),
            ],
            options={
                'verbose_name': 'SEDE',
                'verbose_name_plural': 'SEDES',
            },
        ),
        migrations.CreateModel(
            name='encuentro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resultado_local', models.CharField(choices=[('-', '-'), ('G', 'GANADO'), ('E', 'EMPATADO'), ('P', 'PERDIDO')], default='-', max_length=1)),
                ('resultado_visita', models.CharField(choices=[('-', '-'), ('G', 'GANADO'), ('E', 'EMPATADO'), ('P', 'PERDIDO')], default='-', max_length=1)),
                ('resultado_goles_local', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('resultado_goles_visita', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField(blank=True, null=True)),
                ('humedad', models.CharField(blank=True, max_length=4, null=True)),
                ('clima', models.CharField(blank=True, max_length=4, null=True)),
                ('estado_jugado', models.BooleanField(default=False)),
                ('competicioin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_competicion.competicion')),
            ],
            options={
                'verbose_name': 'ENCUENTRO',
                'verbose_name_plural': 'ENCUENTROS',
            },
        ),
    ]
