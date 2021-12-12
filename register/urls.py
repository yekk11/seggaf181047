from django.urls import path

from . import views

app_name = 'register'

urlpatterns = [

    path('', views.home, name='register'),
    path('signin/', views.signin, name='signin'),
    path('create/', views.create, name='create'),
]
