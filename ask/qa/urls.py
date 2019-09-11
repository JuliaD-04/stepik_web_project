from django.urls import path, include
from . import views

urlpatterns = [
    path('123/', views.test, name="test"),
   
    
]