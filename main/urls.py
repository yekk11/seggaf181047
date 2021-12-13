from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('create/', views.create, name='create'),
    path('del_mhs/<del_id>', views.del_mhs, name='delete-mhs'),
    path('updt_mhs/<up_id>', views.updt_mhs, name='update-mhs'),
]
