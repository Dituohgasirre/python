from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello python world.')


def plot(request):
    X = np.linspace(-np.pi, np.pi, 1000)
    S = np.sin(X)
    C = np.cos(X)
    plt.plot(X, S, 'r-')
    plt.plot(X, C, 'g:')
    im = BytesIO()
    plt.savefig(im, format='png')
    im.seek(0)
    imbytes = im.read()
    return HttpResponse(imbytes, content_type='image/png')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('plot/', plot),
]
