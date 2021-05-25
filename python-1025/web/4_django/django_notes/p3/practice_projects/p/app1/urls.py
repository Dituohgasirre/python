from django.conf.urls import url

from . import views

app_name = "contact"

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^info/([0-9]+)/', views.detail, name='detail'),
]
