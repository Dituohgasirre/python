from django.shortcuts import render, loader, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.db.models import Q
from django.utils import timezone

from .models import Blog, Tag, Author, Category


@csrf_exempt
def blog_list(request):
    """
    滚动更新使用POST方法，GET方法拿的是第一页。
    """
    if request.method == 'POST':        # 这是瀑布流（下一页）请求
        try:
            page = int(request.POST['page'])
        except (KeyError, ValueError):
            return HttpResponseBadRequest('invalid search parameter')
        template_name = "blog/blog_list_scroll.html"
    else:
        page = 1
        template_name = "blog/blog_list.html"

    now = timezone.now()
    blogs = Blog.objects.filter(pub_date__lt=now).order_by('-pub_date')
    end = page * settings.PAGE_SIZE
    start = end - settings.PAGE_SIZE
    total_blogs = blogs.count()
    has_next = total_blogs > end
    blogs = blogs[start:end]

    if request.method == 'POST':
        template = loader.get_template(template_name)
        html = template.render({'blogs': blogs}, request)
        data = {'has_next': has_next, 'html': html}
        return JsonResponse(data)
    else:
        context = {'blogs': blogs, 'page_path': ['All blogs']}
        return render(request, template_name, context=context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/blog_detail.html", context={'blog': blog})


def info(request):
    return render(request, "blog/info.html")


@csrf_exempt
def blog_search(request, author=None, category=None, tag=None):
    """
    滚动更新使用POST方法，GET方法拿的是第一页。
    """
    if request.method == 'POST':
        try:
            page = int(request.POST['page'])
        except (KeyError, ValueError):
            return HttpResponseBadRequest('invalid search parameter')
        template_name = "blog/blog_list_scroll.html"
    else:
        page = 1
        template_name = "blog/blog_list.html"

    if author:
        blogs = Blog.objects.filter(author__pk=author)
        _page_path = ['Author', Author.objects.get(pk=author).name]
    elif category:
        blogs = Blog.objects.filter(category__pk=category)
        _page_path = ['Category', Category.objects.get(pk=category).name]
    elif tag:
        blogs = Blog.objects.filter(tags__in=[tag]).distinct()
        _page_path = ['Tag', Tag.objects.get(pk=tag).name]
    else:
        #
        # keyword format:
        # [type:]keyword
        # example:
        # 1. some keyword           <-- 搜索文章的标题和正文
        # 2. author: some keyword   <-- 搜索作者的名字
        # 3. tag: some keyword      <-- 搜索标签的名字
        #
        try:
            kw = request.GET['s']
        except KeyError:
            return HttpResponseBadRequest('invalid search type')

        if ':' in kw:
            type, kw = kw.split(':', maxsplit=1)
        else:
            type = 'blog'
        kw = kw.strip()

        if type not in ['blog', 'comment', 'author', 'category', 'tag']:
            return HttpResponseBadRequest('invalid search type')

        if type == 'blog':
            cond = Q(title__contains=kw)|Q(content__contains=kw)
            blogs = Blog.objects.filter(cond)
        elif type == 'comment':
            blogs = Blog.objects.filter(comment_set__content__contains=kw)
        elif type == 'author':
            blogs = Blog.objects.filter(author__name__contains=kw)
        elif type == 'category':
            blogs = Blog.objects.filter(category__name__contains=kw)
        elif type == 'tag':
            tags = Tag.objects.filter(name__contains=kw)
            blogs = Blog.objects.filter(tags__in=tags).distinct()

        _page_path = ['Keyword', kw]

    now = timezone.now()
    blogs = blogs.filter(pub_date__lt=now).order_by('-pub_date')
    end = page * settings.PAGE_SIZE
    start = end - settings.PAGE_SIZE
    total_blogs = blogs.count()
    has_next = total_blogs > end
    blogs = blogs[start:end]

    if request.method == 'POST':
        template = loader.get_template(template_name)
        html = template.render({'blogs': blogs}, request)
        data = {'has_next': has_next, 'html': html}
        return JsonResponse(data)
    else:
        context = {'blogs': blogs, 'page_path': ['Search'] + _page_path}
        return render(request, template_name, context=context)
