from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Contact


def index(request):
    contact_list = Contact.objects.all()
    now = datetime.now().strftime('%F %T')
    context = {'data': contact_list, 'current_time': now}
    return render(request, 'app1/index.html', context=context)


def detail(request, contact_id):
    c = get_object_or_404(Contact, pk=contact_id)
    context = {'contact': c}
    return render(request, "app1/detail.html", context=context)
