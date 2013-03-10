# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from facade import comfunc
from character.models import Character,Ability,Stats
from system.models import SetProfessions,Profession,Skill
from forms import EffectForm, SkillForm, ProfessionForm

import string
import operator
from random import randint



def main(request):
    context = RequestContext(request)
    c=Character.objects.get(username='Dulan')
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


    return render_to_response('system/main.html',{"stats":stats,"abilities":abList,"skills":skills},context)



def crtEff(request):
    context = RequestContext(request)
    if request.method == 'POST':
        efform = EffectForm(data=request.POST)
        if efform.is_valid():
            # do some magic here
            print "Define the Effect"
        else:
            print efform.errors
    else:
        efform = EffectForm()

    return render_to_response('system/create/effects.html', {'efform': efform}, context)


def crtSkill(request):
    conext = RequestContext(request)
    if request.method=='POST':
        skillform = SkillForm(data=request.POST)
        if skillform.is_valid():
            # do magic here
            print "Define skill here"
        else:
            print skillform.errors
    else:
        skillform = SkillForm()

    return render_to_response('system/create/skills.html', {'skillform': skillform}, conext)


def crtProf(request):
    context = RequestContext(request)
    if request.method=='POST':
        proform = ProfessionForm(data=request.POST)
        if proform.is_valid():
            # do magics here
            print "Define prof here"
        else:
            print proform.errors
    else:
        proform = ProfessionForm()

    return render_to_response('system/create/prof.html', {'proform': proform}, context)

