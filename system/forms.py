from character.models import Effect
from django import forms

passiv = (('y', 'It is passive'), ('n', 'It is NOT passive'))


class EffectForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="Name the curse or blessing you are creating, Oh mighty GM")
    effect_Formula = forms.CharField(max_length=100, help_text="Describe the law that binds your magical effect")


class SkillForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="Name the technique that will help a hero to fight his enemies.")
    pa = forms.ChoiceField(choices=passiv)
    lvl = forms.IntegerField(max_value=10, help_text="Tell us on whoch lvl is this skill unlocked ?")
    eff = forms.ModelChoiceField(queryset=Effect.objects.all(), help_text="Choose a deadly effect !")


class ProfessionForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="Tell us the name of the Profession you will create in your world")
    # connection with other table
    # ski = forms.ModelChoiceField(queryset=Skill.objects.all(), help_text="Choose a deadly skill for this !")

