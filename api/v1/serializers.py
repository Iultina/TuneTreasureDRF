from rest_framework import serializers
from musical_catalog.models import Artist, Album, Song, AlbumSong

class ArtistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Artist model. It serializes all fields related to a musical artist.
    """
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Album model. It serializes all fields related to a musical album, 
    including details like title, associated artist, and release year.
    """
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    """
    Serializer for the Song model. It serializes all fields related to a musical song, 
    which can be part of multiple albums.
    """
    class Meta:
        model = Song
        fields = '__all__'

class AlbumSongSerializer(serializers.ModelSerializer):
    """
    Serializer for the AlbumSong model. This is an intermediate serializer that captures 
    the many-to-many relationship between songs and albums. It also serializes details 
    like track numbers within an album.
    """
    class Meta:
        model = AlbumSong
        fields = '__all__'
