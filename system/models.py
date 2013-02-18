from django.db import models
from django.forms import CharField
from character.models import *
from gm.models import *

# Create your models here.
class Formula(models.Model):
    formula = models.CharField()

class Weapon(models.Model):
    owner = models.ForeignKey(Character)
    name = models.CharField()

class Misc(models.Model):
    owner = models.ForeignKey(Character)
    name = models.CharField()

class Armor(models.Model):
    owner = models.ForeignKey(Character)
    name = models.CharField()

class Race(models.Model):
    name = models.CharField()
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

class Skill(models.Model):
    prof = models.ForeignKey(Profession)
    name = models.CharField()
    isPassive = models.BooleanField()
    lvl = models.IntegerField()
    effect = models.CharField()

class Profession(models.Model):
    name = models.CharField()
    lvl = models.IntegerField()

class Efect(models.Model):
    name = models.CharField()
    owner = models.ForeignKey(Character)
    effect = models.CharField()
