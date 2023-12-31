# Generated by Django 4.2.4 on 2023-10-30 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_equipo', '0001_initial'),
        ('modulo_contrato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='nuevo_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nuevo_club', to='modulo_equipo.equipo'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_contrato.persona'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='ultimo_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ultimo_club', to='modulo_equipo.equipo'),
        ),
    ]
