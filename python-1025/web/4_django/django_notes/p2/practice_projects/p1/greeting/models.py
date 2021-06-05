from django.db import models


class Log(models.Model):
    text = models.CharField(max_length=4096)
    app = models.CharField(max_length=64)
    value = models.IntegerField(default=0)
    time = models.DateTimeField()
