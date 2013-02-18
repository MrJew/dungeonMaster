from django.db import models
from character.models import *
from system.models import *

# Create your models here.
class GM(models.Model):
    name = models.ForeignKey(User)
    quests = models.ForeignKey(Quest)
    notes = models.ForeignKey(Notes)


class Quest(models.Model):
    creator = models.ForeignKey(GM)
    title = models.CharField(max_length=400)
    snippet = models.CharField()
    xp = models.IntegerField()

class Notes(models.Model):
    creator = models.ForeignKey(GM)
    title = models.CharField()
    snippet = models.CharField(max_length=1000)