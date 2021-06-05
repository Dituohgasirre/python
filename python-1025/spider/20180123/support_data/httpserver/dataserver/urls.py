from django.conf.urls import url

from dataserver import views

urlpatterns = [
    url(r'^get/(?P<kind>[a-z]+)/$', views.get),
    url(r'^post/(?P<kind>[a-z]+)/$', views.post),
]
