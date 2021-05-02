from apps.gifs.models import Gif
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import GifSerializer


class GifViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Gif.objects.all()
    serializer_class = GifSerializer
    permission_classes = [permissions.IsAuthenticated]
