from django.db import models

class Artist(models.Model):
    """
    Model representing a musical artist.
    """
    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def str(self):
        return self.name


class Album(models.Model):
    """
    Model representing a musical album which includes details about the title, 
    its associated artist, and the year of release.
    """
    title = models.CharField(max_length=200, verbose_name='Название')
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name='Исполнитель'
    )
    release_year = models.PositiveIntegerField(verbose_name='Год выпуска')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        unique_together = ('title', 'artist')

    def str(self):
        return self.title


class Song(models.Model):
    """
    Model representing a musical song. Each song can be part of multiple albums.
    """
    title = models.CharField(max_length=200, verbose_name='Название')
    albums = models.ManyToManyField(Album, through='AlbumSong', verbose_name='Альбомы')

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def str(self):
        return self.title


class AlbumSong(models.Model):
    """
    Intermediate model used to capture the many-to-many relationship 
    between songs and albums. Also captures the track number of each song in an album.
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='Песня')
    track_number = models.PositiveIntegerField(verbose_name='Порядковый номер')

    class Meta:
        verbose_name = 'Песня в альбоме'
        verbose_name_plural = 'Песни в альбоме'

    def str(self):
        return f'{self.song.title} (Track {self.track_number} in {self.album.title})'
