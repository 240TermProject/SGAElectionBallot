from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import Vote, Candidate
from django.shortcuts import render, get_object_or_404
from .forms import VoteForm
from django.http import HttpResponseRedirect

def vote_detail(request):
    if request.method == "GET":
        context = {}
        context["candidates"] = []
        for candidate in Candidate.objects.all():
            context["candidates"].append(candidate)
        return render(request, "ballot/vote_detail.html", context)



def cast_votes(request):
    if request.method == "GET":
        context = {}
        context["candidates"] = []
        for candidate in Candidate.objects.all():
            context["candidates"].append(candidate)
        return render(request, "ballot/cast_votes.html", context)
    elif request.method == "POST":
        post = request.POST
        for rank_key, candidate_pk in post.items():
            if rank_key[0:4] == "rank":
                final_rank = int(rank_key[5])
                new_vote = Vote()
                new_vote.rank = final_rank
                new_vote.candidate = Candidate.objects.get(pk=int(candidate_pk))
                new_vote.save()
        return HttpResponseRedirect(reverse("detail"))
