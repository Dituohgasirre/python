from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

from .models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:100]
    context = {'latest_questions': latest_questions}
    return render(request, "polls/index.html", context=context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", context={'q': q})


def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", context={'q': q})


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get('choice', None)
    if choice_id is None:
        error_message = "You have to make a choice"
        return render(request, "polls/detail.html",
                      context={'q': q, 'error_message': error_message})

    choice = get_object_or_404(Choice, question=q, pk=choice_id)
    choice.votes = F('votes') + 1
    choice.save()
    to = reverse('polls:results', args=(question_id,))
    return HttpResponseRedirect(to)
