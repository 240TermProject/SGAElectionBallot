from django.contrib import admin
from .models import Vote
from .models import Candidate

admin.site.register(Vote)
admin.site.register(Candidate)
