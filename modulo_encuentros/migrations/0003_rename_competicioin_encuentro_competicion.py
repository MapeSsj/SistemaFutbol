# Generated by Django 4.2.4 on 2023-10-30 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_encuentros', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encuentro',
            old_name='competicioin',
            new_name='competicion',
        ),
    ]
