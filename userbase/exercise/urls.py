from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('register', views.register, name='register')
]
