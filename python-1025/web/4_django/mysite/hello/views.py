from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def i(request):
    return HttpResponse('<h1>Hello Index</h1>')


def e(request):
    return HttpResponse('<h1>Hello Env</h1> %s' % request)


def http404(request):
    return HttpResponse('<h1>没有找到文件</h1>')
