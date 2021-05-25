from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    create = models.DateTimeField()
