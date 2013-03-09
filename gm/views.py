# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from gm.forms import QuestForm

def createQuest(request):
    if request.method=='POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            quest = form.save()
        else:
            pass
    else:
        form = QuestForm()

