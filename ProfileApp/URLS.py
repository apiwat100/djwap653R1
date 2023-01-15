from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('Home', views.Home, name='Home'),
    path('firstweb', views.firstweb, name='firstweb'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('HNY', views.HNY, name='HNY'),


]
