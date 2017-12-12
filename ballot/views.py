from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import Vote, Candidate, FormatedResultsRow
from django.shortcuts import render, get_object_or_404
from .forms import VoteForm
from django.http import HttpResponseRedirect, HttpResponse
import operator
from random import randint

def vote_detail(request):
    if request.method == "GET":
        context = {}
        context["candidates"] = []
        for candidate in Candidate.objects.all():
            context["candidates"].append(candidate)
        return render(request, "ballot/vote_detail.html", context)

def validate_globalID(request):
    """
    for future use
    """
    pass

def cast_votes(request):
    if request.method == "GET":
        #get request will display drop downs with candidates as options
        context = {}
        context["candidates"] = []
        for candidate in Candidate.objects.all():
            context["candidates"].append(candidate)
        return render(request, "ballot/cast_votes.html", context)
    elif request.method == "POST":
        #post request will submit and format the data for exporting
        post = request.POST
        #creates a list of votes
        vote_list = []
        #crates a list of votes for the specific voter
        new_formated_results_row = FormatedResultsRow()
        #generates a voter id in order to decouple globalID
        voter_id = ("%d%d%d%d%d" %(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)))
        #new_formated_results_row.formated_row = new_formated_results_row.formated_row + voter_id + ": "
        for rank_key, candidate_pk in post.items():
            #takes the context dictionary, extracts the rank, ForeignKey, and cand name, creates a vote object and saves it
            if rank_key[0:4] == "rank":
                final_rank = int(rank_key[5])
                new_vote = Vote()
                new_vote.rank = final_rank
                new_vote.candidate = Candidate.objects.get(pk=int(candidate_pk))
                new_vote.save()
                vote_list.append([new_vote.rank, new_vote.candidate.name])
                #new_formated_results_row.formated_row = new_formated_results_row.formated_row + str(new_vote.rank) + ", " + new_vote.candidate.name + ", "
        #creates a formated row object for the voter and fills it with the previously formated votes and a new line
        new_formated_results_row.formated_row = new_formated_results_row.formated_row + "\n"
        #sorts the votes by rank
        vote_list.sort(key=lambda tup: tup[0])
        #puts the voter ID at the beginning of the list
        vote_list.insert(0, voter_id)
        #writes all the votes to voter_data.txt in templates using python open
        with open('ballot/templates/ballot/voter_data.txt', 'a') as voter_data:
            voter_data.write("%s, " % (vote_list[0]))
            new_formated_results_row.formated_row = new_formated_results_row.formated_row + str(vote_list[0]) + ": "
            for thing in vote_list[1:]:
                #voter_data.write("%d, %s | " % (thing[0], thing[1]))
                voter_data.write("%s, " % (thing[1]))
                new_formated_results_row.formated_row = new_formated_results_row.formated_row + str(thing[1]) + ", "
            voter_data.write("|\n")
            new_formated_results_row.formated_row = new_formated_results_row.formated_row + "\n"
        #print(new_formated_results_row.formated_row)
        return HttpResponseRedirect(reverse("detail"))

def get_results(request):
    #get request sends voter_data to http response and renders as a string at url ~/results so it can be accessed by the actual software
    if request.method == "GET":
        context = {}
        return render(request, "ballot/voter_data.txt", context)
    elif request.method == "POST":
        #for future use if we want to make the file downloadable
        pass
