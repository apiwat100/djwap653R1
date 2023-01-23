from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('Home', views.Home, name='Home'),
    path('edu', views.edu, name='Edu'),
    path('interest', views.interest, name='interest'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('product', views.product, name='Product'),
    path('showdata', views.showdata, name='showdata'),



]
