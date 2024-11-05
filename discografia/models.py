from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from mutagen.mp3 import MP3  # Asegúrate de instalar mutagen para manejar archivos de audio

class Banda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='bandas/')

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('banda-list')

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albumes')
    fecha_lanzamiento = models.DateField()
    portada = models.ImageField(upload_to='albumes/')

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('album-list')

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='canciones')
    genero = models.CharField(max_length=100)  # Nuevo campo género
    audio_file = models.FileField(upload_to='canciones/')
    duracion = models.CharField(max_length=10, editable=False)  # Duración en formato mm:ss
    imagen = models.ImageField(upload_to='canciones/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('cancion-list')

    def save(self, *args, **kwargs):
        # Calcular la duración en mm:ss usando mutagen
        if self.audio_file:
            audio = MP3(self.audio_file)
            minutes, seconds = divmod(int(audio.info.length), 60)
            self.duracion = f"{minutes}:{seconds:02d}"
        super().save(*args, **kwargs)


@receiver(post_delete, sender=Banda)
def team_delete(sender, instance, **kwargs):
     """ Borra los ficheros de las fotos que se eliminan. """
     instance.foto.delete(False)
        
@receiver(post_delete, sender=Album)
def player_delete(sender, instance, **kwargs):
     """ Borra los ficheros de las fotos que se eliminan. """
     instance.portada.delete(False)
     
@receiver(post_delete, sender=Cancion)
def player_delete(sender, instance, **kwargs):
     """ Borra los ficheros de las fotos que se eliminan. """
     instance.imagen.delete(False)