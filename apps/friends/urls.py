from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^register$', views.create),
    url(r'^login$', views.login),
    url(r'^friends$', views.friends),
    url(r'^user/add/(?P<user_id>\d+)/(?P<friend_id>\d+)$', views.addFriend),
    url(r'^user/remove/(?P<user_id>\d+)/(?P<friend_id>\d+)$', views.removeFriend),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^logout$', views.index),
]
