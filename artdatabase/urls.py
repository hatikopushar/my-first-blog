from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('art/', views.art_list, name='art_list'),
    path('art/by-artist-id/<int:artist_id>/', views.art_list, name='art_list'),
    path('art/<int:pk>/', views.art_detail, name='art_detail'),
    path('art/new/', views.art_new, name='art_new'),
    path('art/<int:pk>/edit/', views.art_edit, name='art_edit'),
    path('artist/', views.artist_list, name='artist_list'),
    path('artist/by-name/<str:artist_name>/', views.artist_list, name='artist_list'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('artist/new/', views.artist_new, name='artist_new'),
    path('artist/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
]
