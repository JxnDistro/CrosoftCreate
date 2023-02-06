from django.urls import path
from . import views


urlpatterns = [
    path('', views.landingpage, name='home'),
    path('add_movie', views.add_movie, name='add_movie')
]
