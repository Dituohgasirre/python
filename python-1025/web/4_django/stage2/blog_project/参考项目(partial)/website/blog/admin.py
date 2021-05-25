from django.contrib import admin

from .models import Blog, Author, Category, Tag, Comment, Page, Navi

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Page)
admin.site.register(Navi)
