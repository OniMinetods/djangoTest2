from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('images/', views.image_list, name='images'),
    path('temperature/', views.temperature, name='temperature')
]