from django.urls import path
from . import views

urlpatterns = [

    path('login', views.loginUser, name="login"),

    path('logout', views.logoutUser, name="logout"),

    path('registration', views.registerUser, name='registration'),




    path('', views.photographers, name='photographers'),

    path('photographers/<str:pk>/', views.photographer, name='photographer'),

    path('account', views.createAccount, name='account'),

    path('update', views.updateAccount, name='update'),

    path('device', views.createDevice, name="device"),

    path('updateDevice/<str:pk>/', views.updateDevice, name='updateDevice'),
]
