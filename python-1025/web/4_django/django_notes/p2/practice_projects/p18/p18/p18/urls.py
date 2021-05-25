from django.conf.urls import url
from django.contrib import admin

from store.views import view_settings

urlpatterns = [
    url(r'^', view_settings),
    url(r'^admin/', admin.site.urls),
]
