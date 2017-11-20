from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    name = models.CharField(max_length=200)

class Vote(models.Model):
    rank = models.IntegerField()
    candidate = models.ForeignKey(Candidate)

class Voter(models.Model):
    globalID = models.CharField (max_length=200)
