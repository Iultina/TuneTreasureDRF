from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Artist(models.Model):
    """
    Model representing a musical artist.
    """
    name = models.CharField(max_length=100, verbose_name='Имя')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
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

    def __str__(self):
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

    def __str__(self):
        return self.title


class AlbumSong(models.Model): 
    """ 
    Intermediate model used to capture the many-to-many relationship  
    between songs and albums. Also captures the track number of each song in an album. 
    """ 
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом') 
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='Песня') 
    _track_number = models.PositiveIntegerField(verbose_name='Порядковый номер', editable=False)

    class Meta: 
        verbose_name = 'Песня в альбоме' 
        verbose_name_plural = 'Песни в альбоме' 
        unique_together = ('album', '_track_number')
        constraints = [
            models.UniqueConstraint(
                fields=['song', 'album'],
                name='unique_song_album'
            )
        ]

    def save(self, *args, **kwargs): 
    # Если у экземпляра нет заданного номера трека (то есть он новый), вычисляем следующий доступный номер трека
        if not self._track_number:
            last_track = AlbumSong.objects.filter(album=self.album).order_by('-_track_number').first() 
            if last_track: 
                self._track_number = last_track._track_number + 1 
            else: 
                self._track_number = 1 
        super(AlbumSong, self).save(*args, **kwargs)
 
    def __str__(self): 
        return f'{self.song.title} (Track {self._track_number} in {self.album.title})'

@receiver(post_delete, sender=AlbumSong)
def update_track_numbering(sender, instance, **kwargs):
    """Обновляет нумерацию треков после удаления трека."""
    # Получаем все треки альбома, следующие за удаленным, и обновляем их нумерацию
    tracks_after_deleted = AlbumSong.objects.filter(album=instance.album, _track_number__gt=instance._track_number)
    for track in tracks_after_deleted:
        track._track_number -= 1
        track.save()