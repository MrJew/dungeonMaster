from gm.models import *
from django.forms import *
from django.forms import *
from django import forms
from gm.models import *

class QuestForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(queryset=Character.objects.all())

    class Meta:
        model = Quest
        fields = ("title", "snippet", "xp", "players")
