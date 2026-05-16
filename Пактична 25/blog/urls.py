from django.urls import path
from . import views

urlpatterns = [
    path('media/<int:index>/', views.media_by_index, name='media_detail'),
]