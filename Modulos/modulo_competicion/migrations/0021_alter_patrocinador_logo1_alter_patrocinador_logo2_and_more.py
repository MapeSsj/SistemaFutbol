# Generated by Django 4.2.4 on 2023-10-30 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_competicion', '0020_alter_pais_bandera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrocinador',
            name='logo1',
            field=models.ImageField(blank=True, default='patrocinador/patrocinador_default.png', null=True, upload_to='patrocinador/'),
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='logo2',
            field=models.ImageField(blank=True, default='patrocinador/patrocinador_default.png', null=True, upload_to='patrocinador/'),
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='logo3',
            field=models.ImageField(blank=True, default='patrocinador/patrocinador_default.png', null=True, upload_to='patrocinador/'),
        ),
    ]
