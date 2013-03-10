from gm.models import *
from django import forms

class QuestForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(queryset=Character.objects.all())

    class Meta:
        model = Quest
        fields = ("title", "snippet", "xp", "players")
