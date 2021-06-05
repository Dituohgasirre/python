from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.choice_text
