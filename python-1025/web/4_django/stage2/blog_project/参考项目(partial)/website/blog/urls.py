from django.conf.urls import url
from . import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.blog_list, name="blog_list"),
    url(r'^search/author/(?P<author>[0-9]+)/',
        views.blog_search, name="blog_search_author"),
    url(r'^search/category/(?P<category>[0-9]+)/',
        views.blog_search, name="blog_search_category"),
    url(r'^search/tag/(?P<tag>[0-9]+)/',
        views.blog_search, name="blog_search_tag"),
    url(r'^search/', views.blog_search, name="blog_search"),
    url(r'^(?P<pk>[0-9]+)/', views.blog_detail, name="blog_detail"),
]
