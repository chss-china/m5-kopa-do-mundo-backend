#urls.py
from django.contrib import admin
from django.urls import path

from django.urls import path
from .views import TeamAPIView,TeamDetailView

urlpatterns = [
    
    path('teams/', TeamAPIView.as_view()),
]