# Generated by Django 5.2.2 on 2025-06-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_componente_modelo_3d_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componente',
            name='modelo_3d_url',
        ),
        migrations.AddField(
            model_name='componente',
            name='enlace_modelo_3d',
            field=models.URLField(blank=True, help_text='Pega aquí el enlace al modelo 3D generado por Sketchfab', max_length=500, null=True),
        ),
    ]
