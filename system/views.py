# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from character.models import *
import string, operator

def main(request):
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
              'lvl':c.l}
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