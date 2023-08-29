from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Artist, Album, Song, AlbumSong

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)

@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    exclude = ('_track_number',)

admin.site.unregister(Group)
admin.site.unregister(User)