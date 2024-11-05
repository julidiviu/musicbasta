"""
URL configuration for musica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from discografia import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.discografia_home, name='discografia_home'),
    path('cancion/',views.CancionListView.as_view(),name='cancion-list'),
    path('cancion/<int:pk>/detail/',views.CancionDetailView.as_view(),name='cancion-detail'),
    path('banda/',views.BandaListView.as_view(),name='banda-list'),
    path('banda/<int:pk>/detail/',views.BandaDetailView.as_view(),name='banda-detail'),
    path('album/',views.AlbumListView.as_view(),name='album-list'),
    path('album/<int:pk>/detail/',views.AlbumDetailView.as_view(),name='album-detail'),
    path('cancion/create/',views.CancionCreateView.as_view(), name='cancion-create'),
    path('cancion/<int:pk>/update',views.CancionUpdateView.as_view(), name='cancion-update'),
    path('album/create/',views.AlbumCreateView.as_view(), name='album-create'),
    path('album/<int:pk>/update',views.AlbumUpdateView.as_view(), name='album-update'),
    path('banda/create/',views.BandaCreateView.as_view(), name='banda-create'),
    path('banda/<int:pk>/update',views.BandaUpdateView.as_view(), name='banda-update'),
    path('banda/<int:pk>/delete',views.BandaDelete.as_view(), name='banda-delete'),
    path('album/<int:pk>/delete',views.AlbumDelete.as_view(), name='album-delete'),
    path('cancion/<int:pk>/delete',views.CancionDelete.as_view(), name='cancion-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
