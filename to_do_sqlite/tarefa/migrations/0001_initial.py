# Generated by Django 3.1 on 2020-08-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TarefaBd',
            fields=[
                ('conteudo', models.CharField(max_length=1000)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
