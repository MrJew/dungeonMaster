from django.db import models


# The formula by which a ability/skill is calculated
class Formula(models.Model):
    name = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


# An Effect can be given to a character or to skill/ability
class Effect(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


# Skills can be used from many profesions
class Skill(models.Model):
    name = models.CharField(max_length=50)
    isPassive = models.BooleanField()
    lvl = models.IntegerField()
    effect = models.ManyToManyField(Effect)
    formula = models.ForeignKey(Formula)

    def __unicode__(self):
        return self.name


# A Profession has many skills that have an effect
class Profession(models.Model):
    name = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)

    def __unicode__(self):
        return self.name

from character.models import Character


class SetProfessions(models.Model):
    owner = models.ForeignKey(Character)
    profession = models.ForeignKey(Profession)
    level = models.IntegerField(default=0)
