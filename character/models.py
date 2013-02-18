from django.db import models
from system.models import *
from gm.models import *
from django.contrib.auth.models import User, UserManager

# Create your models here.

class Character(models.Model):
    character = models.ForeignKey(User)
    sp = models.IntegerField()
    race = models.ForeignKey(Race)
    profession = models.ManyToManyField(Profession)
    weapons = models.ManyToManyField(Weapon)
    misc = models.ManyToManyField(Misc)
    armor = models.ManyToManyField(Armor)
    quests = models.ManyToManyField(Quest)

class Stats(models.Model):
    character = models.ForeignKey(Character)
    xp = models.IntegerField()
    race = models.ForeignKey(Race)
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

    def populate(self):
        race = self.race
        str = race.str
        agi = race.agi

class Ability(models.Model):
    name = models.CharField()
    level = models.IntegerField()
    formula = models.ForeignKey(Formula)

