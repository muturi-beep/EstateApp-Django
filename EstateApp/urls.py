from django.urls import path
from EstateApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('gallery/', views.gallery, name='gallery'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact')
]