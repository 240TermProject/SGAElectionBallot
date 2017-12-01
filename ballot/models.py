from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.name

class Vote(models.Model):
    rank = models.IntegerField()
    candidate = models.ForeignKey(Candidate, null=True)

class Voter(models.Model):
    globalID = models.CharField (max_length=200, null=False)
