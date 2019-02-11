from django.conf.urls import url
from django.urls import path

from . import views

app_name = "images"

urlpatterns = [
   url(
       regex=r'^$',
       view=views.Feed.as_view(),
       name='feed'
   ),
   
]