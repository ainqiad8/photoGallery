from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos, name="photos"),
    path('photo/<str:pk>/', views.photo, name='photo'),

    path('create-photo', views.create_photo, name='create-photo'),
    path('update-photo/<str:pk>/', views.update_photo, name='update-photo'),
    path('delete-photo/<str:pk>/', views.delete_photo, name='delete-photo'),
]
