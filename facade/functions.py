from character.models import Stats
from facade.comfunc import dice
from character.models import Log

def checkForFormulaE(string):
    """
    Check if the formating of the Efect is OK
    """
    if string[0] == 'E':
        if string[1]=='(':
            if string[2]=='(':
                return True

    return False


def setStats(user):
    """
     Set the stats for the user, based on hos race
    """
    s = Stats()

    # Set char
    s.character = user
    # Agility
    s.agi = user.race.agi
    s.agiMax = user.race.agiMax
    # Beauty
    s.beauty = dice(3)
    # Dexterity
    s.dex = user.race.dex
    s.dexMax = user.race.dexMax
    # Strength
    s.str = user.race.str
    s.strMax = user.race.strMax
    # Intelligence
    s.int = user.race.int
    s.intMax = user.race.intMax
    # Health
    s.hp = user.race.hp
    # Mana
    s.mana = s.int
    # Speed
    s.speed = user.race.speed
    # Vitality
    s.vitality = user.race.vitality

    s.save()


def writeToLog(character, result):
    logging = Log.objects.get(owner=character)
    logging.text += result
    logging.save()