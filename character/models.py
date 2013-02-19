from django.db import models
from system.models import *
from gm.models import Quest
from django.contrib.auth.models import User, UserManager

# Create your models here.
class Ability(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    formula = models.ForeignKey(Formula)

class Character(models.Model):
    #character = models.ForeignKey(User)
    sp = models.IntegerField()
    profession = models.ManyToManyField(Profession)
    quests = models.ManyToManyField(Quest)
    effects = models.ManyToManyField(Effect)

class Stats(models.Model):
    character = models.ForeignKey(Character)
    xp = models.IntegerField()
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

class Race(models.Model):
    character = models.ForeignKey(Character)
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

class Weapon(models.Model):
    owner = models.ForeignKey(Character)
    name = models.CharField(max_length=50)

class Misc(models.Model):
    owner = models.ForeignKey(Character)
    name = models.CharField(max_length=50)

class Armor(models.Model):
    owner = models.ForeignKey(Character)
    name = models.CharField(max_length=50)