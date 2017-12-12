from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    """
    Candidate class contains only name for formating to the export file
    """
    name = models.CharField(max_length=200)

    #tostring
    def __str__(self):
        return "%s" % self.name

class Vote(models.Model):
    """
    a Vote instance for each candidate for each voter - will become the arraylist
    of arraylists within the actual software
    """
    rank = models.IntegerField()
    candidate = models.ForeignKey(Candidate, null=True)

class Voter(models.Model):
    """
    Voter class is for validation only and does not get attatched to the voter
    data itself
    """
    globalID = models.CharField (max_length=200, null=False)

class FormatedResultsRow(models.Model):
    """
    used for formating - contains a row of votes for each voter
    """
    formated_row = models.CharField (max_length=1000, null=False)

    #tostring
    def __str__(self):
        return "%s" % self.formated_row
