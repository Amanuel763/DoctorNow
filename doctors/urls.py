from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('<int:id>', views.doctor_detail, name='doc_detail')
]   
