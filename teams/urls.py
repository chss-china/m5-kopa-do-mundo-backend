from django.contrib import admin
from django.urls import path
#from . import views

from django.urls import path
from .views import TeamAPIView

urlpatterns = [
    
    path('teams/', TeamAPIView.as_view()),
]