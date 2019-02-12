from django.urls import path
from django.conf.urls import url
from . import views

app_name = "users"
urlpatterns = [
    url(
        regex=r'^explore/$',
        view = views.ExploreUsers.as_view(),
        name = 'explore_users'
    ),
    url(
        regex=r'(?P<user_id>[0-9]+)/follow/$',
        view = views.FollowUser.as_view(),
        name = 'follow_users'
    ),
   url(
       regex=r'(?P<user_id>[0-9]+)/Unfollow/$',
        view = views.UnFollowUser.as_view(),
        name = 'Unfollow_users'
   )
    
]
