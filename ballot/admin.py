from django.contrib import admin
from .models import Vote
from .models import Candidate
from .models import FormatedResultsRow

admin.site.register(Vote)
admin.site.register(Candidate)
admin.site.register(FormatedResultsRow)
