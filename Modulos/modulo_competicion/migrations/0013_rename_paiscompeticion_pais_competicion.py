# Generated by Django 4.2.4 on 2023-10-22 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_competicion', '0012_rename_pais_competicion_paiscompeticion_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaisCompeticion',
            new_name='pais_competicion',
        ),
    ]