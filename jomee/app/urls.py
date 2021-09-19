from django.contrib import admin
from django.urls import path,include
from .views import AlbumListView,AlbumDetailView,SingerListView,SingerDetailView,CommentView,LikeView
from rest_framework.authtoken import views

urlpatterns = [
    path('detail-album/<int:pk>',AlbumDetailView.as_view()),
    path('list-album', AlbumListView.as_view()),
    path('singers', SingerListView.as_view()),
    path('like', LikeView.as_view()),
    path('singers/<int:pk>', SingerDetailView.as_view()),
    path('comment/', CommentView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]
