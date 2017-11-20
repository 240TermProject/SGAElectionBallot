from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.vote_detail, name='detail'),
    url(r'^vote/$', views.cast_votes, name='vote'),
]
