from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import *
from .serializer import AlbumSerializer, TrackSerializer, SingerSerializer


# Create your views here.


class AlbumSerializerListView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackSerializerListView(ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class AlbumSerializerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class show_all_Track(APIView):

    def get(self, reqiest, pk):
        # album = Album.objects.get(id=pk)
        album = Track.objects.all().get(album_id=pk)

        serializer = TrackSerializer(album)
        return Response(serializer.data)

class CommentSerializerView(APIView):
    pass