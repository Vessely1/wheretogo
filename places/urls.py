from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.place_list, name='place_list'),
    path('add/', views.add_place, name='add_place'),
    path('random/', views.random_place, name='random_place'),
    path('place/<int:pk>/', views.place_detail, name='place_detail'),
]