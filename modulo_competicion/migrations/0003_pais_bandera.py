# Generated by Django 4.2.6 on 2023-10-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_competicion', '0002_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='pais',
            name='bandera',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
