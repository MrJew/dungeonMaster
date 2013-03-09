from django.db import models
from system.models import *
#from gm.models import Quest
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

# Create your models here.
# Ability has a one to many relation with the Formulas
class Ability(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    formula = models.ForeignKey(Formula)

    def __unicode__(self):
        return self.name

# Race stores the basic and max stats a character will use
class Race(models.Model):
    name = models.CharField(max_length=50)
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
    sp = models.IntegerField()
    profession = models.ManyToManyField(Profession)
    effects = models.ManyToManyField(Effect)
    race = models.ForeignKey(Race)

    def __unicode__(self):
        return self.username

# Stats containts the statistics a player can have
class Stats(models.Model):
    character = models.ForeignKey(Character)
    level = models.IntegerField(default=0)
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

# Items there are 3 types with several subtypes
class Item(models.Model):
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

    def __unicode__(self):
        return self.item


