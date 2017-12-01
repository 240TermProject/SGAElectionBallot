from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import Vote, Candidate
from django.shortcuts import render, get_object_or_404
from .forms import VoteForm
from django.http import HttpResponseRedirect
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
    pass
    #stuff

def cast_votes(request):
    if request.method == "GET":
        context = {}
        context["candidates"] = []
        for candidate in Candidate.objects.all():
            context["candidates"].append(candidate)
        return render(request, "ballot/cast_votes.html", context)
    elif request.method == "POST":
        post = request.POST
        vote_list = []
        voter_id = ("%d%d%d%d%d" %(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)))
        for rank_key, candidate_pk in post.items():
            if rank_key[0:4] == "rank":
                final_rank = int(rank_key[5])
                new_vote = Vote()
                new_vote.rank = final_rank
                new_vote.candidate = Candidate.objects.get(pk=int(candidate_pk))
                new_vote.save()
                vote_list.append([new_vote.rank, new_vote.candidate.name])
        vote_list.sort(key=lambda tup: tup[0])
        vote_list.insert(0, voter_id)
        with open('voter_data.txt', 'a') as voter_data:
            voter_data.write("%s: " % (vote_list[0]))
            for thing in vote_list[1:]:
                #voter_data.write("%d, %s | " % (thing[0], thing[1]))
                voter_data.write("%s, " % (thing[1]))
            voter_data.write("\n")

        return HttpResponseRedirect(reverse("detail"))
