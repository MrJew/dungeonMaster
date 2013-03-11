
from models import *
from django.forms import *
from django.forms import *
from django import forms
from character.models import *

from gm.models import *
from django import forms



class QuestForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(queryset=Character.objects.all(), widget=CheckboxSelectMultiple)
    snippet = forms.CharField(widget=Textarea)
    class Meta:
        model = Quest
        fields = ("title", "snippet", "xp", "players")

class NotesForm(forms.ModelForm):
    title = forms.CharField(widget=Textarea)
    snippet = forms.CharField(widget=Textarea)
    class Meta:
        model = Notes
        fields = ("title", "snippet")
