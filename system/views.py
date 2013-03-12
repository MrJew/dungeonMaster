# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from facade import comfunc
from character.models import Character, Ability, Stats, Log

from facade.comfunc import *
from character.models import Character, Ability, Stats

from system.models import SetProfessions, Profession, Skill
from django.core.management.base import CommandError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from facade.comfunc import dice
from facade.functions import writeToLog


from character.models import Stats
from forms import EffectForm, SkillForm, ProfessionForm

from models import Effect, Skill, Profession
from facade.functions import checkForFormulaE

import string
import operator
from random import randint


def main(request):
    context = RequestContext(request)
    character = Character.objects.get(pk=request.user.id)
    s = Stats.objects.get(character=character)
    stats = getBaseStats(character)

    abilities = Ability.objects.all()
    abList=[]
    for i in abilities:
        abList.append({"name":i.name,"value":getStat(character,i)})

    charInfo=getChar(character)
    quests = getQuests(character)
    armor = getArmor(character)
    weapon = getWeapon(character)
    misc = getMisc(character)

    prof = []
    professions = SetProfessions.objects.filter(owner=character)
    for profession in professions:
        skills = []
        for skill in profession.profession.skills.all():
            if skill.lvl<=profession.level:
                skills.append(skill)
        prof.append({"skills":skills,"name":profession.profession.name,'lvl':profession.level})

    print prof

    return render_to_response('system/main.html',{"stats":stats,"abilities":abList,"prof":prof,
                                                  'char':charInfo,"quests":quests,"weapons":weapon,
                                                  'armor':armor,"misc":misc},context)


def crtEff(request):
    """
    Form for creating an effect
    """
    context = RequestContext(request)
    correct = False
    if request.method == 'POST':
        efform = EffectForm(data=request.POST)
        if efform.is_valid():
            # do some magic here
            if Effect.objects.filter(name=efform.cleaned_data['effect_formula']).count() <= 0:
                correct = checkForFormulaE(efform.cleaned_data['effect_formula'])
                if correct:
                    e = Effect()
                    e.name = efform.cleaned_data['name']
                    e.effect = efform.cleaned_data['name']
                    e.save()

                    return render_to_response('system/main.html', {'correct': correct}, context)
                else:
                    print "Error the check not correct"
            else:
                print "Effect like this exists"
        else:
            print efform.errors
    else:
        efform = EffectForm()

    return render_to_response('system/create/effects.html', {'efform': efform, 'correct': correct}, context)


def crtSkill(request):
    """
    Form for creating a skill
    """
    context = RequestContext(request)
    if request.method=='POST':
        skillform = SkillForm(data=request.POST)
        if skillform.is_valid():
            if Skill.objects.filter(name=skillform.cleaned_data['name']).count() <= 0:
                s = Skill()
                s.name = skillform.cleaned_data['name']
                s.lvl = skillform.cleaned_data['lvl_unlock']

                if skillform.cleaned_data['condition'] == 'y':
                    s.isPassive = True
                else:
                    s.isPassive = False
                s.save()
                s.effect = skillform.cleaned_data['effect']
                s.save()
                return render_to_response('system/main.html', {'skillform': skillform}, context)
            else:
                print "cant add"
                raise CommandError("Can't create entry-> entry already exists ")
        else:
            print skillform.errors
    else:
        skillform = SkillForm()

    return render_to_response('system/create/skills.html', {'skillform': skillform}, context)


def crtProf(request):
    """
    Form for creating a profession
    """
    context = RequestContext(request)
    if request.method == 'POST':
        proform = ProfessionForm(data=request.POST)
        if proform.is_valid():
            if Profession.objects.filter(name=proform.cleaned_data['name']).count() <= 0:
                p = Profession()
                p.name = proform.cleaned_data['name']
                p.save()
                p.skills = proform.cleaned_data['skills']
                p.save()

                return render_to_response('system/main.html', {'proform': proform}, context)
            else:
                print "Value already exists"
        else:
            print proform.errors
    else:
        proform = ProfessionForm()

    return render_to_response('system/create/prof.html', {'proform': proform}, context)


def char_login(request):
    """
    login a user character/gm
    """
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("system.views.main",  args=()))
            else:
                return HttpResponse("You're account is disabled")
        else:
            pass
    else:
        return render_to_response('login/login.html', context)

@login_required
def char_logout(request):
    """
    logout a character/gm
    """
    context = RequestContext(request)
    logout(request)
    return HttpResponseRedirect(reverse("system.views.char_login", args=()))


def show_log(request):
    """
    Show the log based on the Char ID
    """
    # define the models !
    listOf_logs = ""
    for element in Log.objects.all():
        listOf_logs += str(element.getText())
        listOf_logs += " </br>"
    return HttpResponse(listOf_logs)


def roll(request):
    result = "Your mighty result is ["+str(dice(1))+"]</br>"
    character = Character.objects.get(pk=request.user.id)
    writeToLog(character, result)

    return HttpResponse()
