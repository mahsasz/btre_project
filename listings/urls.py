from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name = 'listings'), #inja yani safeye index bara listings ine
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),
    # dalile inke inja nemigim listings/search ine ke in gharare link beshe b urls aslimoon va begim k
    # har chizi ke hast listings/ marboot b in file mishe link mishe be in urls.py dar listings
]
