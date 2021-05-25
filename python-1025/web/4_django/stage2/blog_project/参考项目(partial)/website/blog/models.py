from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=16777216)
    author = models.ForeignKey('Author')
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')
    pub_date = models.DateTimeField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=16777216, blank=True, null=True)


class Comment(models.Model):
    content = models.TextField(max_length=16384)
    blog = models.ForeignKey('Blog')
    to = models.ForeignKey('Comment', blank=True, null=True)
    pub_date = models.DateTimeField()


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('Category', blank=True, null=True)


class Page(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=16777216)


NAVI_TYPES = [('external', 'External'),
              ('internal', 'Internal'),
              ('category', 'Category'),
              ('page', 'Page'),
        ]


class Navi(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(choices=NAVI_TYPES, max_length=16)
    target = models.CharField(max_length=512)
    left = models.BooleanField(default=1)
    order = models.IntegerField(default=0)
