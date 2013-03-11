
from models import *
from django.forms import *
from django.forms import *
from django import forms
from character.models import *

from gm.models import *
from django import forms



class QuestForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(queryset=Character.objects.all(), help_text="Which heroes will go on this quest?", widget=CheckboxSelectMultiple)
    snippet = forms.CharField(widget=Textarea, help_text="What adventures does the quest entail?")
    title = forms.CharField(help_text="What is the title of your quest?")
    xp = forms.IntegerField(help_text="How much experience does the quest grant?")
    class Meta:
        model = Quest
        fields = ("title", "snippet", "xp", "players")

class NotesForm(forms.ModelForm):
    title = forms.CharField(widget=Textarea)
    snippet = forms.CharField(widget=Textarea)
    class Meta:
        model = Notes
        fields = ("title", "snippet")
