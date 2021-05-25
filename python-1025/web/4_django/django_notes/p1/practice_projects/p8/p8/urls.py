from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^monitor/', include('monitor.urls')),
    url(r'^admin/', admin.site.urls),
]
