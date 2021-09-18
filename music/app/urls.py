from django.urls import path
from .views import AlbumSerializerListView, TrackSerializerListView, AlbumSerializerDetailView,show_all_Track

urlpatterns = [
    path('album_list/', AlbumSerializerListView.as_view(), name="albumlist"),
    path('track_list/', TrackSerializerListView.as_view(), name="track_list"),
    path('album_etail/<int:pk>', AlbumSerializerDetailView.as_view(), name="albumlist"),

    path('tracklist/<int:pk>',show_all_Track.as_view(), name = "tracklist"),

]
