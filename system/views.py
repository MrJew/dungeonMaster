# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response


from character.models import Stats
from forms import EffectForm, SkillForm, ProfessionForm

import string
import operator
from random import randint



def main(request):
    print "Tva e viewto na maina"
    context = RequestContext(request)
    return render_to_response('system/main.html',context)



def rpn(s):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    while True:
        st = []
        for tk in string.split(s):
            print tk
            if tk in ops:
                print "operator"
                y,x = st.pop(),st.pop()
                z = ops[tk](x,y)
            else:
                print "str"
                z = int(tk)
            st.append(z)
        assert len(st)<=1
        if len(st)==1:
            print(st.pop())
            break


def getValues(c):
    s = Stats.objects.get(character=c)
    values = {'agi': s.getAgi(),
              'str': s.getStr(),
              'int': s.getInt(),
              'dex': s.getDex(),
              'vit': s.getVit(),
              'speed': s.getSpeed(),
              'beauty': s.getBeauty(),
              'lvl':s.xp/1000,
              'dice': randint(1,6)}
    return values

def formToString(s,v):
    st = string.split(s)
    final=""
    for i in st:
        if len(i)>2:
            final+=str(v[i])
        else:
            final+=i
        final+=" "
    return final


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

