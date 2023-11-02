# Generated by Django 4.2.6 on 2023-10-22 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temporada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('modalidad', models.CharField(choices=[('EUROPEA', 'EUROPEA'), ('LIGA', 'LIGA'), ('Copa de Europa (UEFA Champions League)', 'Copa de Europa (UEFA Champions League)'), ('TORNEO', 'TORNEO'), ('COPA PAIS', 'COPA PAIS')], max_length=100)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]