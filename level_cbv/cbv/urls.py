from django.urls import path
from cbv import views

app_name = 'cbv'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>', views.SchoolDetailedView.as_view(), name='detail')
]