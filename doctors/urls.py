from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('<int:id>', views.doctor_detail, name='doctor_detail'),
    path('search', views.search, name='search'),
]   
