
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('pic/', views.index, name='index'),
    path('pic2/', views.index3, name='index3'),
    path('sw.js', (TemplateView.as_view(template_name="sw.js",content_type='application/javascript', )), name='sw.js'),
]