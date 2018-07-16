from django.urls import path
from cbv import views

app_name = 'cbv'

urlpatterns = [
    path('', views.IndexView.as_view())
]