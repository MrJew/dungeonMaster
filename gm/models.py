from django.db import models
from character.models import *
from system.models import *
from django.contrib.auth.models import User, UserManager


# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=50)
    snippet = models.CharField(max_length=1000)

class Quest(models.Model):
    title = models.CharField(max_length=50)
    snippet = models.CharField(max_length=400)
    xp = models.IntegerField()


class GM(models.Model):
    name = models.ForeignKey(User)
    quests = models.ForeignKey(Quest)
    notes = models.ForeignKey(Notes)

