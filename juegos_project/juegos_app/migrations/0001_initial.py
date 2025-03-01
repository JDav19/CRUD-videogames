# Generated by Django 5.1.6 on 2025-02-25 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('precio', models.CharField(default='DEFAULT VALUE', max_length=20)),
                ('stock', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('img', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
