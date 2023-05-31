from django.contrib import admin
from django.urls import path
#from . import views

from django.urls import path
from .views import TeamAPIView,TeamDetailView

urlpatterns = [
    
    path('teams/', TeamAPIView.as_view()),
    path('teams/<int:pk>/', TeamDetailView.as_view()),
]