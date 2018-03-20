from rest_framework import generics, permissions
from rest_framework.views import APIView

from artist.serializers import ArtistSerializer
from utils.pagination import StandardResultsSetPagination
from ...models import Artist
from rest_framework.response import Response

__all__ = (
    'ArtistListCreateView',
    'ArtistRetrieveUpdateDestroyView',
)


class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        print('request.user:', request.user)
        return super().get(request, *args, **kwargs)


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination
