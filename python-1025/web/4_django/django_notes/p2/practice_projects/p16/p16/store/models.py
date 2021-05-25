from django.db import models


class Father(models.Model):
    name = models.CharField(max_length=16)

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
