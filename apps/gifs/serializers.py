from apps.gifs.models import Gif
from rest_framework import serializers
from apps.tags.serializers import TagSerializer


class GifSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Gif
        fields = ['name', 'gif', 'tags']