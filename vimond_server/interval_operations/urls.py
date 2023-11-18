from django.urls import path
from . import views

app_name = 'interval_operations'

urlpatterns = [
    path('api/process_intervals/', views.api_process_intervals, name='api_process_intervals'),
    path('', views.html_process_intervals, name='html_process_intervals'),
]