from character.models import Stats
from system.models import  Formula
from gm.models import Quest
import string, operator
from random import randint

################################Common Functions for stats, formulas and calculations##########################################################

def rpn(s):
    """
    RPN calculator that takes a string and returns a result
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
    """
    returns the value of an ability for the specified character
    """
    return formulaResult(ability.formula.formula,character)

def getQuests(character):
    return Quest.objects.filter(players=character)

def getChar(character):
    values = getValues(character)
    char= {"name":character.username,
           "xp":values['xp'],
           "lvl":values['lvl'],
           "hp":values['hp'],
           "mana":values['mana'],
           "sp":values['sp']}

    return char

def hpLvl(character):
    """
    gets the ammount of hp character gets per level
    """
    stats = Stats(character=character)
    return dice(int(stats.getStr())/2)/3

def spLvl(character):
    """
    gets the amount of skill points character gets per level
    """
    stats = Stats(character=character)
    return dice(int(stats.getInt())/2)/3

def getAP(character):
    """
    gets the action points a player has
    """
    formula = Formula.objects.get(name="Action Points")
    return formulaResult(formula,character)

def formulaResult(formula,character):
    """
    returns a the result from a fiven formula
    """
    values = getValues(character)
    return rpn(formulaToString(formula,values))

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
              'xp': s.xp,
              'lvl':s.xp/1000,
              'hp':s.getHP,
              'mana':s.getMana,
              'sp': s.sp,
              'dice': dice(3)}
    return values

def formulaToString(formula,values):
    """
    Converts a formula string eg.( str 3 + dex / ) into a understandable string for the rpn calculator
    """
    st = string.split(formula)
    final=""
    for i in st:
        if not str.isdigit(str(i)) and i!="+" and i!="-" and i!="*" and i!="/":
            final+=str(values[i])
        else:
            final+=i
        final+=" "
    return final

def dice(dn=None):
    """
    roll any number of six sided dices
    """
    if not dn:
        dn=1
    total=0
    for i in range(dn):
        m=randint(1,6)
        total+= m

    return total



