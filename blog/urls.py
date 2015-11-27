from django.conf.urls import url

from .views import *

urlpatterns=[
    url(r'^posts/$', list_posts, name='list_posts'),
    url(r'^posts/(?P<pk>\d+)/$', view_posts, name='view_posts'),
    url(r'^posts/create/$', create_posts, name='create_posts'),
    url(r'^posts/(?P<pk>\d+)/edit/$', edit_posts, name='edit_posts'),
    url(r'^posts/(?P<pk>\d+)/delete/$', delete_posts, name='delete_posts'),
]
