from django.conf.urls import url
from . import views

#get module called views from current dir

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.index, name='index'),

    # default section - index, or homepage for each app
    # if nothing is included like music/ , then it will be handled by default here ^$
    # ^$ matches all, by RegEx
    # name is optional

    # /music/<albumID>
    # e.g. /music/71

    # this will be saved as album_id variable
    # match digits 0-9, any number, ignore '/'
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail" ),


    # /music/<album_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),
]



