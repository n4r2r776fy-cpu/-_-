from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('media/', views.media_detail, name='media'), # Новий маршрут для завдання на 5 балів
]