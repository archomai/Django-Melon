from rest_framework.views import APIView

from artist.serializers import ArtistSerializer
from ...models import Artist
from rest_framework.response import Response

__all__ = (
    'ArtistListView',
)


class ArtistListView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)