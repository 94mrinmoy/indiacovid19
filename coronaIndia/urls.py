
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('pic/', views.index, name='index'),
    path('pic2/', views.index3, name='index3'),
]