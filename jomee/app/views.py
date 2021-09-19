from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import *
from .serializers import AlbumListSerializer,TrackSerializer,CommentSerializer,AlbumDetailSerializer,SingerListSerializer,SingerDetailSerializer


class AlbumListView(APIView):

    def get(self, request, format=None):
        album = Album.objects.all()
        serializer = AlbumListSerializer(album, many=True)
        return Response(serializer.data)

class AlbumDetailView(APIView):

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data)




class SingerListView(APIView):

    def get(self, request, format=None):
        singer = Singer.objects.all()
        serializer = SingerListSerializer(singer, many=True)
        return Response(serializer.data)

class SingerDetailView(APIView):

    def get_object(self, pk):
        try:
            return Singer.objects.get(pk=pk)
        except Singer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        singer = self.get_object(pk)
        serializer = SingerDetailSerializer(singer)
        return Response(serializer.data)


class AlbumDetailView(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        album = self.get_object(pk)
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data)


class CommentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        track_id = request.data.get("track", None)
        if not Track.objects.filter(id=track_id).exists():
            return Response({
                "successful": False,
                "err": True,
                "message": "track id not valid"
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentSerializer(
            data=request.data, context={"request": request,"user":request.user})

        if serializer.is_valid():
            serializer.save()

            return Response({
                "successful": True,
                "err": False,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "successful": False,
            "err": True,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class LikeView (APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        album_id = request.data.get("album", None)
        if not Album.objects.filter(id=album_id).exists():
            if not cache.get(f"like_{album_id}"):
                cache.set(f"like_{album_id}", [])
            likes = list(cache.get(f"like_{album_id}"))
            if request.user.id in likes:
                print(likes)
                likes.remove(request.user.id)
                cache.set(f"like_{album_id}", likes)
                return Response({
                    "successful": True,
                    "err": False,
                    "message": "disliked"
                })
            else:
                print(likes)
                likes=likes.append(request.user.id)
                cache.set(f"like_{album_id}", likes)
                return Response({
                    "successful": True,
                    "err": False,
                    "message": "liked"
                })