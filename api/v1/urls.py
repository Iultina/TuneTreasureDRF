from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlbumSongViewSet, AlbumViewSet, ArtistViewSet, SongViewSet

app_name = 'api_v1'

router = DefaultRouter()
router.register(r'artists', ArtistViewSet, basename='artists')
router.register(r'albums', AlbumViewSet, basename='albums')
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'album-songs', AlbumSongViewSet, basename='album-songs')

urlpatterns = [
    path('', include(router.urls)),
]
