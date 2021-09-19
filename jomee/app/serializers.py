from rest_framework import serializers

from .models import Track, Album, Singer, User, Comment


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'


class AlbumListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['title','singer']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data,**kwargs):
        user_id= self.context.get("user")
        return Comment.objects.create(user=user_id, **validated_data)


class TrackSerializer(serializers.ModelSerializer):
    track = CommentSerializer(many=True)

    class Meta:
        model = Track
        fields = '__all__'




class AlbumDetailSerializer(serializers.ModelSerializer):
    album = TrackSerializer(many=True)


    class Meta:
        model = Album
        fields = "__all__"


class SingerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'


class SingerDetailSerializer(serializers.ModelSerializer):
    singer = AlbumDetailSerializer(many=True)

    class Meta:
        model = Singer
        fields = "__all__"

