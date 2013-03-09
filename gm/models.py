from django.db import models
from character.models import *
from system.models import *
from django.contrib.auth.models import User, UserManager


# Create your models here.

class GM(User):

    def __unicode__(self):
        return self.username

# Notes created from gm
class Notes(models.Model):
    gm = models.ForeignKey(GM)
    title = models.CharField(max_length=50)
    snippet = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.title

# GM craetes quesets that can be assigned to players after that
class Quest(models.Model):
    gm = models.ForeignKey(GM)
    title = models.CharField(max_length=50)
    snippet = models.CharField(max_length=400)
    xp = models.IntegerField()

    def __unicode__(self):
        return self.title


