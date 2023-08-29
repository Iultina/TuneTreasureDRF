from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from musical_catalog.models import Artist, Album, Song, AlbumSong

class ArtistTests(APITestCase):

    def setUp(self):
        self.artist = Artist.objects.create(name='Sample Artist')
        self.url = reverse('artist-list')

    def test_create_artist(self):
        """
        Ensure we can create a new artist.
        """
        data = {'name': 'Test Artist'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 2)
        self.assertEqual(Artist.objects.get(id=response.data['id']).name, 'Test Artist')

    def test_read_artist(self):
        """
        Ensure we can read an artist.
        """
        response = self.client.get(f"{self.url}{self.artist.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.artist.name)

    def test_update_artist(self):
        """
        Ensure we can update an artist.
        """
        updated_name = 'Updated Artist Name'
        data = {'name': updated_name}
        response = self.client.put(f"{self.url}{self.artist.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artist.refresh_from_db()
        self.assertEqual(self.artist.name, updated_name)

    def test_delete_artist(self):
        """
        Ensure we can delete an artist.
        """
        response = self.client.delete(f"{self.url}{self.artist.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), 0)


class AlbumTests(APITestCase):

    def setUp(self):
        self.artist = Artist.objects.create(name='Test Artist')
        self.album = Album.objects.create(title='Sample Album', artist=self.artist, release_year=2019)
        self.url = reverse('album-list')

    def test_create_album(self):
        """
        Ensure we can create a new album.
        """
        data = {
            'title': 'Test Album',
            'artist': self.artist.id,
            'release_year': 2020
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 2)
        self.assertEqual(Album.objects.get(id=response.data['id']).title, 'Test Album')

    def test_read_album(self):
        """
        Ensure we can read an album.
        """
        response = self.client.get(f"{self.url}{self.album.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.album.title)

    def test_update_album(self):
        """
        Ensure we can update an album.
        """
        updated_title = 'Updated Album Title'
        data = {
            'title': updated_title,
            'artist': self.artist.id,
            'release_year': 2021
        }
        response = self.client.put(f"{self.url}{self.album.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.album.refresh_from_db()
        self.assertEqual(self.album.title, updated_title)

    def test_delete_album(self):
        """
        Ensure we can delete an album.
        """
        response = self.client.delete(f"{self.url}{self.album.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), 0)



class SongTests(APITestCase):

    def setUp(self):
        self.song = Song.objects.create(title='Sample Song')
        self.url = reverse('song-list')

    def test_create_song(self):
        """
        Ensure we can create a new song.
        """
        data = {'title': 'Test Song'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 2)
        self.assertEqual(Song.objects.get(id=response.data['id']).title, 'Test Song')

    def test_read_song(self):
        """
        Ensure we can read a song.
        """
        response = self.client.get(f"{self.url}{self.song.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.song.title)

    def test_update_song(self):
        """
        Ensure we can update a song.
        """
        updated_title = 'Updated Song Title'
        data = {'title': updated_title}
        response = self.client.put(f"{self.url}{self.song.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.song.refresh_from_db()
        self.assertEqual(self.song.title, updated_title)

    def test_delete_song(self):
        """
        Ensure we can delete a song.
        """
        response = self.client.delete(f"{self.url}{self.song.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Song.objects.count(), 0)


class AlbumSongTests(APITestCase):

    def setUp(self):
        self.artist = Artist.objects.create(name='Test Artist')
        self.album = Album.objects.create(title='Sample Album', artist=self.artist, release_year=2019)
        self.song = Song.objects.create(title='Sample Song')
        self.album_song = AlbumSong.objects.create(album=self.album, song=self.song, track_number=1)
        self.url = reverse('albumsong-list')

    def test_create_albumsong(self):
        """
        Ensure we can create a new album-song relationship.
        """
        data = {
            'album': self.album.id,
            'song': self.song.id,
            'track_number': 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AlbumSong.objects.count(), 2)

    def test_read_albumsong(self):
        """
        Ensure we can read an album-song relationship.
        """
        response = self.client.get(f"{self.url}{self.album_song.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['track_number'], self.album_song.track_number)

    def test_update_albumsong(self):
        """
        Ensure we can update an album-song relationship.
        """
        updated_track_number = 3
        data = {
            'album': self.album.id,
            'song': self.song.id,
            'track_number': updated_track_number
        }
        response = self.client.put(f"{self.url}{self.album_song.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.album_song.refresh_from_db()
        self.assertEqual(self.album_song.track_number, updated_track_number)

    def test_delete_albumsong(self):
        """
        Ensure we can delete an album-song relationship.
        """
        response = self.client.delete(f"{self.url}{self.album_song.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AlbumSong.objects.count(), 0)