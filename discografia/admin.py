from django.contrib import admin
from .models import Banda, Album, Cancion

@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'banda', 'fecha_lanzamiento')
    list_filter = ('banda', 'fecha_lanzamiento')
    search_fields = ('titulo', 'banda__nombre')

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'banda', 'duracion', 'genero')
    list_filter = ('album', 'banda')
    search_fields = ('titulo', 'album__titulo', 'banda__nombre')
