from django.forms import *
from django import forms
from gm.models import *

class QuestForm(forms.ModelForm):
    title = forms.CharField()
    snippet = forms.CharField()
    xp = forms.IntegerField()
    choice = forms.ChoiceField(User.objects.all())

#class Meta:
 #   model = Quest
  #  fields = ("title", "snippet", "xp", "players")
