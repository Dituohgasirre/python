from django.conf.urls import url

from .views import login, captcha

app_name = 'polls'

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^captcha/', captcha, name='captcha'),
]
