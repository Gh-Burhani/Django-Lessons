from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('microsoftbing/', views.microsoftbing, name='microsoftbing'),
    path('chat/', views.chat, name='chat'),
    path('images/', views.images, name='images'),
    path('videos/', views.videos, name='vedieos'),
    path('maps/', views.maps, name='maps'),
    path('news/', views.news, name='news'),
    
]