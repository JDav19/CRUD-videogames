from django.db import models
from django.core.exceptions import ValidationError

# Validación personalizada para el campo de imagen
def validate_image_extension(value):
    if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        raise ValidationError('Solo se permiten archivos PNG, JPG, JPEG o GIF.')

class Juego(models.Model):  # Nombre de la tabla en la Base de Datos
    # Opciones para el campo 'género'
    GENDER_CHOICES = [
        ('ACC', 'Acción'),
        ('AVT', 'Aventura'),
        ('DEP', 'Deportes'),
        ('EST', 'Estrategia'),
        ('RPG', 'RPG'),
        ('OTR', 'Otro'),
    ]

    # Opciones para el campo 'clasificacion_edad'
    CLASIFICATION_CHOICES = [
        ('E', 'Para todos'),
        ('E10+', 'Para mayores de 10 años'),
        ('T', 'Para adolescentes'),
        ('M', 'Para adultos'),
        ('AO', 'Solo adultos'),
    ]

    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # DecimalField para precios
    stock = models.IntegerField(default=0)  # IntegerField para el stock
    img = models.FileField(upload_to='juegos/', validators=[validate_image_extension])  # FileField para la imagen con validación
    genero = models.CharField(max_length=3, choices=GENDER_CHOICES, default='OTR')  # ChoiceField para el género
    clasificacion_edad = models.CharField(max_length=4, choices=CLASIFICATION_CHOICES, default='E')  # ChoiceField para la clasificación
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'juegos'  # Nombre de instancia con la que llamamos la tabla en la Base de Datos

    def __str__(self):
        return self.nombre  # Representación legible del objeto