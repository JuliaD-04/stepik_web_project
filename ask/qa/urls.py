from django.urls import path, include
from qa.views import test

urlpatterns = [
    path('', test),
    re_path(r'^(?P<id>\d+)/$', test, name="test"),
   
    
]