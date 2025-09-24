from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'), # Отслеживание динамического параметра
    path('data/', views.getData, name='get_data'),
    path('data/<int:pk>/', views.getDataNumber, name='get_data_number')
]