from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [

    path('', views.home, name='home'),
    path('vcenkripsi/', views.vcenkripsi, name='vcenkripsi'),
    path('vcdekripsi/', views.vcdekripsi, name='vcdekripsi'),
    path('caesarenc/', views.caesarenc, name='caesarenc'),
    path('caesardec/', views.caesardec, name='caesardec'),
    path('lsbembed/', views.lsbembed, name='lsbembed'),
    path('lsbextract/', views.lsbextract, name='lsbextract'),

]
