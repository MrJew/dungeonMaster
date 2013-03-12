from character.models import *
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

def existInPlayers(player,players):
    for p in players:
        if p==player:
            return True
    return False

def getPlayers(gm):
    """
    Gets the players a Gm is working with
    """
    players=[]
    for quest in Quest.objects.filter(gm=gm):
        for player in quest.players.all():
            if not existInPlayers(player,players):
                players.append(player)
    return players

def getStat(character,ability):
    """
    returns the value of an ability for the specified character
    """
    return formulaResult(ability.formula.formula,character)

def getQuests(character):
    """
    gets the quests of a player
    """
    return Quest.objects.filter(players=character)

def getArmor(character):
    """
    gets all the armor type items from a player
    """
    return Inventory.objects.filter(owner=character,type="A")

def getMisc(character):
    """
    gets all the misc type items from a player
    """
    return Inventory.objects.filter(owner=character,type="M")

def getWeapon(character):
    """
    gets all the weapon type items from a player
    """
    return Inventory.objects.filter(owner=character,type="W")

def getBaseStats(character):
    """
    gets the basic statistics of a player
    """
    s = Stats.objects.get(character=character)
    stats = [{'name':"Agility",'stat': s.getAgi()},
             {'name':"Strength",'stat': s.getStr()},
             {'name':"Inteligence",'stat': s.getInt()},
             {'name':"Dexterity",'stat': s.getDex()},
             {'name':"Vitality",'stat': s.getVit()},
             {'name':"Speed",'stat': s.getSpeed()},
             {'name':"Beauty",'stat': s.getBeauty()},
             {'name':"Level",'stat':s.xp/1000},
             ]
    return stats

def getChar(character):
    """
    get character info statistics
    """
    values = getValues(character)
    char= {"name":character.username,
           "xp":values['xp'],
           "lvl":values['lvl'],
           "hp":values['hp'],
           "mana":values['mana'],
           "sp":values['sp'],
           "ap":values['ap']}

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
              'ap': s.ap,
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



