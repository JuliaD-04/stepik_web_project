from django.urls import path, include
from qa.views import test
# from . import views
from django.urls import re_path

urlpatterns = [
    path('', test, ),
    re_path(r'^(?P<id>\d+)/$', test, name="test"),
   
    
]