# Generated by Django 4.0.1 on 2022-01-31 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_animal', models.CharField(max_length=20)),
                ('predador', models.CharField(max_length=5)),
                ('venenoso', models.CharField(max_length=5)),
                ('domestico', models.CharField(max_length=5)),
            ],
        ),
    ]
