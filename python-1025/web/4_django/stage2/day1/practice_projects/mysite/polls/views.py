import hashlib
from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Q
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Question, Choice, User
from .forms import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # age = form.cleaned_data['age']
            # cell = form.cleaned_data['cell']
            return HttpResponse('successfully signed up.')

    else:   # get method
        form = UserForm()

    return render(request, "polls/signup.html", context={'form': form})




def gen_sid(text):
    return hashlib.sha1(text.encode()).hexdigest()


def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username, password=password):
                # 登录成功了
                delta = timedelta(days=1)
                expire_time = timezone.now() + delta
                session_data = expire_time.strftime('%s')
                session_id = gen_sid('%s:%s' % (username, session_data))
                request.session[session_id] = session_data
                url = reverse('polls:index')
                r = HttpResponseRedirect(url)
                r.set_cookie('sid', session_id, int(delta.total_seconds()))
                return r
            else:
                error_message = "login failed"
                context = {'form': form, 'error_message': error_message}
                return render(request, "polls/login.html", context=context)
    else:
        form = UserForm()
    return render(request, "polls/login.html", context={'form': form})


def logout(request):
    sid = request.COOKIES.get('sid', None)
    response = HttpResponseRedirect(reverse('polls:login'))
    if sid is not None:
        del request.session[sid]
        response.delete_cookie(sid)
    return response


def index(request):
    now = timezone.now()
    latest_questions = Question.objects.filter(pub_date__lt=now).order_by('-pub_date')
    context = {'latest_questions': latest_questions}
    r = render(request, "polls/index.html", context=context)
    return r


class QuestionList(ListView):
    model = Question
    # queryset = Question.objects.filter(pub_date__lt=timezone.now()).order_by('-pub_date')
    template_name = "polls/index.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        now = timezone.now()
        latest_questions = self.model.objects.filter(pub_date__lt=now).order_by('-pub_date')
        return latest_questions

    def get_context_data(self, *args, **kargs):
        context = ListView.get_context_data(self, *args, **kargs)
        context['now'] = timezone.now()
        return context


def detail(request, question_id):
    now = timezone.now()
    q = get_object_or_404(Question, pk=question_id, pub_date__lt=now)
    return render(request, "polls/detail.html", context={'q': q})


def results(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", context={'q': q})


class QuestionDetail(DetailView):
    model = Question
    template_name = "polls/detail.html"
    context_object_name = 'q'


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
