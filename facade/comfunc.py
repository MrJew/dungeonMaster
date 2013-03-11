from character.models import Stats
import string, operator
from random import randint

#######################################Common Functions##########################################################

def rpn(s):
    """ RPN calculator that takes a string and returns a result
    """
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    while True:
        st = []
        for tk in string.split(s):
            if tk in ops:
                y,x = st.pop(),st.pop()
                z = ops[tk](x,y)
            else:
                z = int(tk)
            st.append(z)
        assert len(st)<=1
        if len(st)==1:
            return st.pop()
            break

def getStat(character,ability):
    values = getValues(character)
    formString = formulaToString(ability.formula.formula,values)
    print ability.name,formString
    result = rpn(formString) + int(ability.level)
    return result


def getValues(c):
    """ Returns in a dictionary the values of a player
    """
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

def formulaToString(s,v):
    """ Converts a formula string eg.( str 3 + dex / ) into a understandable string for the rpn calculator
    """
    st = string.split(s)
    final=""
    for i in st:
        if not str.isdigit(str(i)) and i!="+" and i!="-" and i!="*" and i!="/":
            final+=str(v[i])
        else:
            final+=i
        final+=" "
    return final

def dice(dn=None):
    if not dn:
        dn=1
    total=0
    for i in range(dn):
        m=randint(1,6)
        total+= m

    return total

###########################################Stats Functions##########################################################

