from django.urls import path, include
# from qa.views import test
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.test, name="test"),
    re_path(r'^ "" (?P< id >\d+)/$', views.test, name="test"),
   
    
]