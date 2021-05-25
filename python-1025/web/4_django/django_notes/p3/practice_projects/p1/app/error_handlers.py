from django.http import HttpResponse


def page_not_found(request, exception):
    html = '<h1 style="color: red">Error occurred.</h1>'
    return HttpResponse(html, status=404)
