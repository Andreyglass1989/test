from django.conf.urls import url
from .views import (
	all_users,
	user_posts,
	post_id,
	#PostView,
	CreatePostView,
	UpdatePostView,
	)


urlpatterns = [
	
	url(r'^(?P<pk>\d+)/update/$', UpdatePostView.as_view()),
	url(r'^create/$', CreatePostView.as_view()),	
	#url(r'^(?P<id>\d+)/$', PostView.as_view()),	
	url(r'^(?P<id>\d+)/$', post_id),
	url(r'^users/(?P<pk>\d+)/$', user_posts),
    url(r'^users/', all_users, name="main"),
    
]
