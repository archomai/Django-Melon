from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from artist.apis import ArtistListCreateView, ArtistRetrieveUpdateDestroyView

app_name = 'artist'
urlpatterns = [
    path('', ArtistListCreateView.as_view(), name='artist-list'),
    path('<int:pk>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)