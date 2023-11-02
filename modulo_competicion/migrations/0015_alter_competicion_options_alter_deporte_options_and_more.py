# Generated by Django 4.2.4 on 2023-10-23 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_competicion', '0014_alter_competicion_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competicion',
            options={'verbose_name': 'COMPETICION', 'verbose_name_plural': 'COMPETICIONES'},
        ),
        migrations.AlterModelOptions(
            name='deporte',
            options={'verbose_name': 'DEPORTE', 'verbose_name_plural': 'DEPORTES'},
        ),
        migrations.AlterModelOptions(
            name='entidad',
            options={'verbose_name': 'ENTIDAD', 'verbose_name_plural': 'ENTIDADES'},
        ),
        migrations.AlterModelOptions(
            name='formato',
            options={'verbose_name': 'FORMATO', 'verbose_name_plural': 'FORMATOS'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'PAIS', 'verbose_name_plural': 'PAISES'},
        ),
        migrations.AlterModelOptions(
            name='pais_competicion',
            options={'verbose_name': 'PAIS ASIGNADOS A COMPETICIONES DE FUTBOL', 'verbose_name_plural': 'PAISES ASIGNADOS A COMPETICIONES DE FUTBOL'},
        ),
        migrations.AlterModelOptions(
            name='temporada',
            options={'verbose_name': 'TEMPORADA', 'verbose_name_plural': 'TEMPORADAS'},
        ),
        migrations.AlterModelOptions(
            name='tipo_competicion',
            options={'verbose_name': 'TIPO DE COMPETICION', 'verbose_name_plural': 'TIPO DE COMPETICIONES'},
        ),
        migrations.AlterModelOptions(
            name='tipo_equipo',
            options={'verbose_name': 'TIPO DE EQUIPO', 'verbose_name_plural': 'TIPO DE EQUIPOS'},
        ),
        migrations.CreateModel(
            name='patrocinador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_oficial', models.CharField(max_length=70)),
                ('nombre_corto', models.CharField(max_length=40)),
                ('abreviatura', models.CharField(max_length=8)),
                ('logo1', models.CharField(blank=True, max_length=255, null=True)),
                ('logo2', models.CharField(blank=True, max_length=255, null=True)),
                ('logo3', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('competicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_competicion.competicion')),
            ],
        ),
    ]