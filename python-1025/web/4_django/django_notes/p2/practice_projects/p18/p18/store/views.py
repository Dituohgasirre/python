from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


def view_settings(request):
    import pdb
    pdb.set_trace()
    keys = ':'.join(settings.__dict__)
    return HttpResponse(keys)
