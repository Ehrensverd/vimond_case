# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("api/interval-processor/", views.process_intervals, name="interval-processor"),
]
