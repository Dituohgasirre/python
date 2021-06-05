from django.db import models


class Log(models.Model):
    time = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.CharField(max_length=16384)
    pid = models.IntegerField(default=0)
    uid = models.IntegerField()
    gid = models.IntegerField()

    def __str__(self):
        return self.text[:30]
