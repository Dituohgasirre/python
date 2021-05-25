from django.conf.urls import url, include
from django.contrib import admin

# from app import error_handlers

handler404 = 'app.error_handlers.page_not_found'

urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
]
