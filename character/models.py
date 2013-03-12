from django.db import models
from system.models import Effect,Formula
from django.contrib.auth.models import User, UserManager



Item_CHOICES=(("Sword","Sword"),
              ("Bow","Bow"),
              ("Axe","Axe"),
              ("Mace","Mace"),
              ("Wand","Wand"),
              ("Staff","Staff"),
              ("Dagger","Dagger"),
              ("Ring","Ring"),
              ("Amulet","Amulet"),
              ("Missile","Missile"),
              ("Potion","Potion"),
              ("Magic Artifact","Magic Artifact"),
              ("Shield","Shield"),
              ("Chest","Chest"),
              ("Helm","Helm"),
              ("Gloves","Gloves"),
              ("Pants","Pants"),
              ("Boots","Boots"),
              ("Belt","Belt"),
              ("Other","Other"))

item_types=(("Armor","A"),
            ("Weapon","W"),
            ("Misc","M"))


# Race stores the basic and max stats a character will use
class Race(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()
    str = models.IntegerField()
    strMax = models.IntegerField()
    agi = models.IntegerField()
    agiMax = models.IntegerField()
    int = models.IntegerField()
    intMax = models.IntegerField()
    dex = models.IntegerField()
    dexMax = models.IntegerField()
    vitality = models.IntegerField()
    speed = models.IntegerField()

    def __unicode__(self):
        return self.name

# Character contains the User model and the objects it's composed of
class Character(User):
    # default params
    effects = models.ManyToManyField(Effect)
    race = models.ForeignKey(Race)

    def __unicode__(self):
        return self.username

class Log(models.Model):
    """
    Character logs for console are stored here
    """
    owner = models.ForeignKey(Character)
    text = models.TextField(max_length=20000)

    def getText(self):
        return self.text

# Stats containts the statistics a player can have
class Stats(models.Model):
    character = models.ForeignKey(Character)
    ap = models.IntegerField(default=0)
    apMod = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    hpMod = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    manaMod = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    str = models.IntegerField()
    strMax = models.IntegerField()
    strMod = models.IntegerField(default=0)
    agi = models.IntegerField()
    agiMax = models.IntegerField()
    agiMod = models.IntegerField(default=0)
    int = models.IntegerField()
    intMax = models.IntegerField()
    intMod = models.IntegerField(default=0)
    dex = models.IntegerField()
    dexMax = models.IntegerField()
    dexMod = models.IntegerField(default=0)
    vitality = models.IntegerField()
    vitMod = models.IntegerField(default=0)
    speed = models.IntegerField()
    speedMod = models.IntegerField(default=0)
    beauty = models.IntegerField()
    beautyMod = models.IntegerField(default=0)

    def getHP(self):
        return self.hp + self.getVit() + self.hpMod

    def getMana(self):
        return self.mana + self.getInt() + self.manaMod

    def getStr(self):
        return self.str + self.strMod

    def getAgi(self):
        return self.agi + self.agiMod

    def getInt(self):
        return self.int + self.intMod

    def getDex(self):
        return self.dex + self.dexMod

    def getBeauty(self):
        return self.beauty + self.beautyMod

    def getSpeed(self):
        return self.speed + self.speedMod

    def getVit(self):
        return self.vitality + self.vitMod



class Item(models.Model):
    """Items there are 3 types with several subtypes"""
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=40,choices=Item_CHOICES)
    dmg = models.CharField(max_length=100)
    ap = models.IntegerField(blank=True,default=0)
    defence = models.IntegerField(blank=True,default=0)
    effect = models.ManyToManyField(Effect)
    attack = models.ForeignKey(Formula)
    weight = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.name

class Inventory(models.Model):
    owner = models.ForeignKey(Character)
    item = models.ForeignKey(Item)
    durability = models.IntegerField()
    equiped = models.BooleanField()
    type = models.CharField(max_length=40,choices=item_types)



from facade import comfunc

# Create your models here.
# Ability has a one to many relation with the Formulas
class Ability(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    formula = models.ForeignKey(Formula)

    def __unicode__(self):
        return self.name



