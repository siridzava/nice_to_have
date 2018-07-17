from django.urls import path
from cbv import views

app_name = 'cbv'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>', views.SchoolDetailedView.as_view(), name='detail'),
    path('create/<int:pk>', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'),
]