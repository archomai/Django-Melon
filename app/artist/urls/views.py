from django.urls import path

from .. import views

app_name = 'artist'
urlpatterns = [
    # artist_list view가
    # /artist/ 에서 출력되도록 path설정
    path('', views.artist_list, name='artist-list'),

    path('add/', views.artist_add, name='artist-add'),

    path('<int:artist_pk>/', views.artist_detail, name='artist-detail'),

    path('<int:artist_pk>/edit/', views.artist_edit, name='artist-edit'),

    path('<int:artist_pk>/like-toggle/', views.artist_like_toggle, name='artist-like-toggle'),

    path('<int:artist_pk>/add-youtube/', views.artist_add_youtube, name='artist-add-youtube'),

    path('search/melon/', views.artist_search_from_melon, name='artist-search-from-melon'),

    path('search/melon/add/', views.artist_add_from_melon, name='artist-add-from-melon'),
]
