from apps.tags.models import Tag
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

