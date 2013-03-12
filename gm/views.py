# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from gm.forms import QuestForm, NotesForm
from gm.models import GM, Notes, Quest
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from character.models import *
from facade.comfunc import *

def createQuest(request):
    context = RequestContext(request)
    if request.POST.get('submit'):
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
            return HttpResponseRedirect(reverse('maingm'))
        else:
            print form.errors
    elif request.POST.get('cancel'):
        return HttpResponseRedirect(reverse('maingm'))
    else:
        form = QuestForm()

    return render_to_response('gm/quest/quest.html', {'form': form}, context)

def editQuest(request,quest_id):
    context = RequestContext(request)
    quest = Quest.objects.get(pk=quest_id)
    if request.POST.get('submit'):
        form = QuestForm(request.POST)
        if form.is_valid():
            # quest.gm trqbva da se napravi da vzima avtomati4no gm-a
            quest.gm = GM.objects.get(username='Entaria')
            quest.title = form.cleaned_data['title']
            quest.snippet = form.cleaned_data['snippet']
            quest.xp = form.cleaned_data['xp']
            quest.save()
            quest.players = form.cleaned_data['players']
            quest.save()
            return HttpResponseRedirect(reverse('maingm'))
        else:
            print form.errors
    elif request.POST.get('cancel'):
        return HttpResponseRedirect(reverse('maingm'))
    else:
        players=[]
        for p in quest.players.all():
            players.append(p.id)
        form = QuestForm(initial={"title":quest.title,"snippet":quest.snippet,"xp":quest.xp,"players":players})

    return render_to_response('gm/quest/quest.html', {'form': form}, context)

def createNotes(request):
    context = RequestContext(request)
    if request.POST.get('submit'):
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes()
            # quest.gm trqbva da se napravi da vzima avtomati4no gm-a
            notes.gm = GM.objects.get(username='Entaria')
            notes.title = form.cleaned_data['title']
            notes.snippet = form.cleaned_data['snippet']
            notes.save()
            return HttpResponseRedirect(reverse('maingm'))
        else:
            print form.errors
    elif request.POST.get('cancel'):
        return HttpResponseRedirect(reverse('maingm'))
    else:
        form = NotesForm()

    return render_to_response('gm/notes/notes.html', {'form': form}, context)

def editNotes(request,notes_id):
    """
    edit your own notes
    """
    context = RequestContext(request)
    notes = Notes.objects.get(pk=notes_id)
    if request.POST.get('submit'):
        form = NotesForm(request.POST)
        if form.is_valid():
            # quest.gm trqbva da se napravi da vzima avtomati4no gm-a
            notes.gm = GM.objects.get(username='Entaria')
            notes.title = form.cleaned_data['title']
            notes.snippet = form.cleaned_data['snippet']
            notes.save()
            return HttpResponseRedirect(reverse('createNotes'))
        else:
            print form.errors
    elif request.POST.get('cancel'):
        return HttpResponseRedirect(reverse('maingm'))
    else:
        form = NotesForm(initial={"title":notes.title,"snippet":notes.snippet})

    return render_to_response('gm/notes/notes.html', {'form': form}, context)

def giveItem(request,player_id):
    context = RequestContext(request)
    item_id = request.POST.get('item',False)
    item = Item.objects.get(pk=item_id)
    character = Character.objects.get(pk=player_id)
    i = Inventory(owner=character,item=item,durability=20,type="M")
    i.save()
    return HttpResponseRedirect(reverse('maingm'))

def giveEffect(request,player_id):
    """
    gm gives effects to a player
    """
    context = RequestContext(request)
    effect_id = request.POST.get('effect',False)
    effect = Item.objects.get(pk=effect_id)
    character = Character.objects.get(pk=player_id)

    character.effects.add(effect)
    character.save()
    return HttpResponseRedirect(reverse('maingm'))

def giveXP(request,player_id):
    """
    gm gives xp to a player
    """
    context = RequestContext(request)
    ammount = request.POST.get('number',False)
    character = Character.objects.get(pk=player_id)
    stats = Stats.objects.get(character=character)
    lvl = stats.xp/1000
    stats.xp = stats.xp + ammount
    if stats.xp/1000 > lvl:
        stats.sp=stats.sp + spLvl(character)

    stats.save()
    return HttpResponseRedirect(reverse('maingm'))

