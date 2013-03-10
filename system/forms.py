from character.models import Effect
from models import Skill
from django import forms

passiv = (('y', 'It is passive'), ('n', 'It is NOT passive'))


class EffectForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="Name the curse or blessing you are creating, Oh mighty GM")
    effect_formula = forms.CharField(max_length=100, help_text="Describe the law that binds your magical effect")


class SkillForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="Name the technique that will help a hero to fight his enemies.",
                           required=True)
    condition = forms.ChoiceField(choices=passiv)
    lvl_unlock = forms.IntegerField(max_value=10, help_text="Tell us on whoch lvl is this skill unlocked ?")
    effect = forms.ModelMultipleChoiceField(queryset=Effect.objects.all(), help_text="Choose a deadly effect !",
                                            widget=forms.CheckboxSelectMultiple, required=True)


class ProfessionForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="Tell us the name of the Profession you will create in your world",
                           required=True)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), help_text="Choose a deadly effect !",
                                            widget=forms.CheckboxSelectMultiple, required=True)


