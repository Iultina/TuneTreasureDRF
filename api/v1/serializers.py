from rest_framework import serializers
from musical_catalog.models import Artist, Album, Song, AlbumSong

class ArtistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Artist model. It serializes all fields related to a musical artist.
    """
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Album model. It serializes all fields related to a musical album, 
    including details like title, associated artist, and release year.
    """
    artist = serializers.PrimaryKeyRelatedField(queryset = Artist.objects.all())

    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'release_year')


class SongSerializer(serializers.ModelSerializer):
    """
    Serializer for the Song model. It serializes all fields related to a musical song, 
    which can be part of multiple albums.
    """

    class Meta: 
        model = Song 
        fields = ('id', 'title', 'albums')


class AlbumSongSerializer(serializers.ModelSerializer):
    """
    Serializer for the AlbumSong model. This is an intermediate serializer that captures 
    the many-to-many relationship between songs and albums. It also serializes details 
    like track numbers within an album.
    """
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    song = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all())

    class Meta: 
        model = AlbumSong 
        fields = ('album', 'song', '_track_number')

    def get_album(self, obj):
        return obj.album.id, obj.album.title

    def get_song(self, obj):
        return obj.song.id, obj.song.title
