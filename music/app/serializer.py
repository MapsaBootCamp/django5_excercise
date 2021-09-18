from rest_framework import serializers

from .models import Album, Track, Singer


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ["name"]


class AlbumSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()

    class Meta:
        model = Album
        fields = ["title", "singer"]


class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Track
        fields = "__all__"
