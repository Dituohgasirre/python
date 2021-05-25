from django.db import models
from django.utils import timezone


class Father(models.Model):
    name = models.CharField(max_length=16)
    btime = models.DateTimeField(auto_now_add=True, blank=True)
    mtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Child(models.Model):
    name = models.CharField(max_length=16)
    father = models.ForeignKey(Father, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Tag(models.Model):
    desc = models.CharField(max_length=128)

    def __str__(self):
        return '<%s>' % self.desc

    def __repr__(self):
        return self.__str__()


class Article(models.Model):
    title = models.CharField(max_length=128)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return '<%s>' % self.title

    def __repr__(self):
        return self.__str__()


class Public(models.Model):
    keyid = models.CharField(max_length=128)

    def __str__(self):
        return '<%s>' % self.keyid

    def __repr__(self):
        return self.__str__()


class Private(models.Model):
    keyid = models.CharField(max_length=128)
    other = models.OneToOneField(Public, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '<%s>' % self.keyid

    def __repr__(self):
        return self.__str__()
