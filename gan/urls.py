from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('uploadimg/',views.upload,name='upload'),
    path('getcaption/',views.getcaption,name='getcaption'),

    #path('base/',views.base,name="base"),

]