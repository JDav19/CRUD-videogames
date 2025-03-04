# Generated by Django 5.1.6 on 2025-03-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='clasificacion_edad',
            field=models.CharField(choices=[('E', 'Para todos'), ('E10+', 'Para mayores de 10 años'), ('T', 'Para adolescentes'), ('M', 'Para adultos'), ('AO', 'Solo adultos')], default='E', max_length=4),
        ),
        migrations.AddField(
            model_name='juego',
            name='genero',
            field=models.CharField(choices=[('ACC', 'Acción'), ('AVT', 'Aventura'), ('DEP', 'Deportes'), ('EST', 'Estrategia'), ('RPG', 'RPG'), ('OTR', 'Otro')], default='OTR', max_length=3),
        ),
        migrations.AlterField(
            model_name='juego',
            name='img',
            field=models.FileField(upload_to='juegos/'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='juego',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='juego',
            table='juegos',
        ),
    ]
