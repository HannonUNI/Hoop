from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contest(models.Model):
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name + '\n' + self.auther + '\n' + self.status + '\n' + str(self.start_time) + '\n' + str(self.end_time)


class Question(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    instructions = models.CharField(max_length=255)
    solution = models.TextField(max_length=10000)
    score = models.IntegerField()
    # status = models.CharField(max_length=40)

    def __str__(self):
        return self.name + '\n' + str(self.time_limit) + '\n' + self.instructions + '\n' + self.solution + '\n' + str(self.score)


class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.question.name + '\n' + self.user.username + '\n' + self.code


class User_Contest(models.Model):
    # make user and contest unique together
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'contest'], name='unique_user_contest'
            )
        ]

    def __str__(self):
        return self.user.username + '\n' + self.contest.name + '\n' + str(self.score)
