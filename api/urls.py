from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:room_name>/', views.room, name='room'),
]