from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from discografia.models import Cancion
from discografia.models import Banda
from discografia.models import Album

# Create your views here.
from django.views.generic import ListView
from .models import Cancion


def discografia_home(request):
    return render(request, 'discografia/home.html')
    template_name = 'discografia/home.html'

class CancionListView(ListView):
    model = Cancion
    template_name = 'cancion_list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset

class CancionDetailView(DetailView):
    model = Cancion
    context_object_name = 'cancion'


class BandaListView(ListView):
    model = Banda
    template_name = 'banda_list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Banda.objects.filter(nombre__icontains=query)
        return Banda.objects.all()


class BandaDetailView(DetailView):
    model = Banda
    template_name =  template_name = 'discografia/banda_detail.html'
    context_object_name = 'banda'


class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Album.objects.filter(titulo__icontains=query).order_by('fecha_lanzamiento')
        return Album.objects.all().order_by('fecha_lanzamiento')


class AlbumDetailView(DetailView):
    model = Album
    template_name =  template_name = 'discografia/album_detail.html'
    context_object_name = 'album'
    
# Vista para Crear Banda
class BandaCreateView(CreateView):
    model = Banda
    fields = ['nombre', 'descripcion', 'foto']
    template_name = 'discografia/banda_form.html'  
    success_url = reverse_lazy('banda-list')

# Vista para Editar Banda
class BandaUpdateView(UpdateView):
    model = Banda
    fields = ['nombre', 'descripcion', 'foto']
    template_name = 'discografia/banda_form.html'  
    success_url = reverse_lazy('banda-list')
    
class AlbumCreateView(CreateView):
    model = Album
    fields = ['titulo', 'banda', 'fecha_lanzamiento', 'portada']
    template_name = 'discografia/album_form.html'  
    success_url = reverse_lazy('album-list')

# Vista para Editar Álbum
class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['titulo', 'banda', 'fecha_lanzamiento', 'portada']
    template_name = 'discografia/album_form.html'  
    success_url = reverse_lazy('album-list')
    
class CancionCreateView(CreateView):
    model = Cancion
    fields = ['titulo', 'album', 'banda', 'audio_file', 'imagen', 'genero']
    template_name = 'discografia/cancion_form.html'  
    success_url = reverse_lazy('cancion-list')

# Vista para Editar Canción
class CancionUpdateView(UpdateView):
    model = Cancion
    fields = ['titulo', 'album', 'banda', 'audio_file', 'imagen']
    template_name = 'discografia/cancion_form.html'  
    success_url = reverse_lazy('cancion-list')
    
class BandaDelete(DeleteView):
    model = Banda
    success_url = reverse_lazy('banda-list')
    
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('album-list')
    
class CancionDelete(DeleteView):
    model = Cancion
    success_url = reverse_lazy('cancion-list')
    
def estadisticas(request):
    # Calcular el total de bandas, álbumes y canciones
    total_bandas = Banda.objects.count()
    total_albumes = Album.objects.count()
    total_canciones = Cancion.objects.count()

    # Calcular el número de canciones por género
    canciones_por_genero = Cancion.objects.values('genero').annotate(total=Count('id'))

    context = {
        'total_bandas': total_bandas,
        'total_albumes': total_albumes,
        'total_canciones': total_canciones,
        'canciones_por_genero': list(canciones_por_genero),  # Convertir a lista para JavaScript
    }

    return render(request, 'discografia/estadisticas.html', context)