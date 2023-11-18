from django.urls import path
from . import views

app_name = 'interval_operations'

urlpatterns = [
    path('api/process_intervals/', views.process_intervals, name='api_process_intervals'),
    path('', views.process_intervals, name='process_intervals'),
]