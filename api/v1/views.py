from rest_framework import viewsets

from musical_catalog.models import Album, AlbumSong, Artist, Song

from .serializers import (AlbumSerializer, AlbumSongSerializer,
                          ArtistSerializer, SongSerializer)


class ArtistViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations related to the Artist model.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations related to the Album model.
    This includes operations for individual albums and their associated artist.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations related to the Song model.
    Songs can be part of multiple albums.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumSongViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations related to the AlbumSong intermediate model.
    This model captures the relationship between songs and albums, including track numbers.
    """
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer
