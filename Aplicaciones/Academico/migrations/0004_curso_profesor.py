# Generated by Django 5.1.4 on 2024-12-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_remove_curso_periodo_inscripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
