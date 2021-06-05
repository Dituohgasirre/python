from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotFound, Http404
from django.views.decorators.http import require_POST


def login(request):
    raise Http404('xx')


def inbox(request):
    return HttpResponse('This is the inbox')
