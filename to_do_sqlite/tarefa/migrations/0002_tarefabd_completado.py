# Generated by Django 3.1 on 2020-08-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefabd',
            name='completado',
            field=models.BooleanField(default=False),
        ),
    ]
