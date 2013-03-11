# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from gm.forms import QuestForm, NotesForm
from gm.models import GM, Notes, Quest
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def createQuest(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            quest = Quest()
            # quest.gm trqbva da se napravi da vzima avtomati4no gm-a
            quest.gm = GM.objects.get(username='Entaria')
            quest.title = form.cleaned_data['title']
            quest.snippet = form.cleaned_data['snippet']
            quest.xp = form.cleaned_data['xp']
            quest.save()
            quest.players = form.cleaned_data['players']
            quest.save()
            return HttpResponseRedirect(reverse('createNotes'))
        else:
            print form.errors
    else:
        form = QuestForm()

    return render_to_response('gm/quest/quest.html', {'form': form}, context)

def createNotes(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes()
            # quest.gm trqbva da se napravi da vzima avtomati4no gm-a
            notes.gm = GM.objects.get(username='Entaria')
            notes.title = form.cleaned_data['title']
            notes.snippet = form.cleaned_data['snippet']
            notes.save()
            return HttpResponseRedirect(reverse('createNotes'))
        else:
            print form.errors
    else:
        form = NotesForm()

    return render_to_response('gm/notes/notes.html', {'form': form}, context)

def showQuests(request):
    context = RequestContext(request)
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('createNotes'))
    else:
        qList = Quest.objects.all()
        quests = []
        for quest in qList:
            quests.append({'title': quest.title, 'snippet': quest.snippet})
        return render_to_response('gm/questDisplay.html', {'quests': quests}, context)
