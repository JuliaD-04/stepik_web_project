from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test, name="test"),
    re_path(r'^(?P<id>\d+)/$', views.test, name="test"),
   
    
]