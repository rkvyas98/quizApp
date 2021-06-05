# from typing_extensions import Required
from django.db import models
# Create your models here.

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200, default=None)
    option4 = models.CharField(max_length=200, default=None)
    option5 = models.CharField(max_length=200, default=None)
    answer = models.IntegerField()
    subject = models.CharField(max_length=20)

    def __str__(self):
        return str(self.question_id) + ": "+ self.question


class Test_stat(models.Model):
    test_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    score = models.IntegerField()
    subject = models.CharField(max_length=20)

    def __str__(self):
        return str(self.test_id) + ": "+ self.username+" subject: "+ self.subject