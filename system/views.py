# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from facade import comfunc
from character.models import Character,Ability,Stats
from system.models import SetProfessions,Profession,Skill
from django.core.management.base import CommandError

from character.models import Stats
from forms import EffectForm, SkillForm, ProfessionForm

from models import Effect, Skill, Profession
from facade.functions import checkForFormulaE

from gm.models import Quest

import string
import operator
from random import randint



def main(request):
    context = RequestContext(request)
    c = Character.objects.get(username='Dulan')
    s = Stats.objects.get(character=c)
    stats = [{'name':"Agility",'stat': s.getAgi()},
                      {'name':"Strength",'stat': s.getStr()},
                      {'name':"Inteligence",'stat': s.getInt()},
                      {'name':"Dexterity",'stat': s.getDex()},
                      {'name':"Vitality",'stat': s.getVit()},
                      {'name':"Dexterity",'stat': s.getSpeed()},
                      {'name':"Beauty",'stat': s.getBeauty()},
                      {'name':"Level",'stat':s.xp/1000},
                      ]

    abilities = Ability.objects.all()
    abList=[]
    for i in abilities:
        abList.append({"name":i.name,"value":comfunc.getStat(c,i)})

    skills = []
    professions = SetProfessions.objects.filter(owner=c)
    for profession in professions:
        for skill in profession.profession.skills.all():
            if skill.lvl<=profession.level:
                skills.append(skill)
    qList = Quest.objects.all()
    quests = []
    for quest in qList:
        quests.append({'title': quest.title, 'snippet': quest.snippet})

    return render_to_response('system/main.html',{"stats":stats,"abilities":abList,"skills":skills, "quests": quests},context)



def crtEff(request):
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

                return  render_to_response('system/main.html', {'proform': proform}, context)
            else:
                print "Value already exists"
        else:
            print proform.errors
    else:
        proform = ProfessionForm()

    return render_to_response('system/create/prof.html', {'proform': proform}, context)

