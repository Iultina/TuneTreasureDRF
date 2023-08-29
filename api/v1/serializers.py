from rest_framework import serializers
from musical_catalog.models import Artist, Album, Song, AlbumSong

class ArtistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Artist model. It serializes all fields related to a musical artist.
    """
    class Meta:
        model = Artist
        fields = ('name',)

class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Album model. It serializes all fields related to a musical album, 
    including details like title, associated artist, and release year.
    """
    artist = serializers.StringRelatedField()

    class Meta:
        model = Album
        fields = ('title', 'artist', 'release_year')


class AlbumTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title')

class SongSerializer(serializers.ModelSerializer):
    """
    Serializer for the Song model. It serializes all fields related to a musical song, 
    which can be part of multiple albums.
    """
    # albums = AlbumTitleSerializer(many=True, read_only=True)
    albums = serializers.StringRelatedField(many=True)

    class Meta: 
        model = Song 
        fields = ('title', 'albums')

class AlbumSongSerializer(serializers.ModelSerializer):
    """
    Serializer for the AlbumSong model. This is an intermediate serializer that captures 
    the many-to-many relationship between songs and albums. It also serializes details 
    like track numbers within an album.
    """
    album = serializers.SerializerMethodField()
    song = serializers.SerializerMethodField()
    _track_number = serializers.IntegerField(read_only=True) 

    class Meta: 
        model = AlbumSong 
        fields = ('album', 'song', '_track_number')

    def get_album(self, obj):
        return obj.album.id, obj.album.title

    def get_song(self, obj):
        return obj.song.id, obj.song.title
