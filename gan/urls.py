from django.contrib import admin
from django.urls import path,include
from gan.image_captioning import image_captioning,Vocabulary
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('uploadimg/',views.upload,name='upload'),
    path('getcaption/',views.getcaption,name='getcaption'),
    path('origin/',views.origin,name='origin'),

    #path('base/',views.base,name="base"),

]