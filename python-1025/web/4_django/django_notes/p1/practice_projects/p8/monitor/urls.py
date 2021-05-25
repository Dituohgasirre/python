from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<task>[a-z]+)/', views.sysinfo),
]
