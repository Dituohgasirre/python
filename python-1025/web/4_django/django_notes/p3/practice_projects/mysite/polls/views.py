from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, "polls/index.html", context=context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", context={'q': q})


def results(request):
    ...


def vote(request):
    ...
