from django.db import models

class Formula(models.Model):
    formula = models.CharField(max_length=100)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    isPassive = models.BooleanField()
    lvl = models.IntegerField()
    effect = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=50)
    lvl = models.IntegerField()
    skills = models.ManyToManyField(Skill)

    def __unicode__(self):
        return self.name

class Effect(models.Model):
    name = models.CharField(max_length=50)
    effect = models.CharField(max_length=100)

