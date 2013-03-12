__author__ = 'ivaylo'
from character.models import *
from django import forms
from system.models import Effect, Formula


# Define some stuff here
users = (('g', 'gm'), ('h', 'hero'))

ARMOR_CHOICES=(("Shield","Shield"),
               ("Chest","Chest"),
               ("Helm","Helm"),
               ("Gloves","Gloves"),
               ("Pants","Pants"),
               ("Boots","Boots"),
               ("Belt","Belt"))

WEAPON_CHOICES=(("Sword","Sword"),
                ("Bow","Bow"),
                ("Axe","Axe"),
                ("Mace","Mace"),
                ("Wand","Wand"),
                ("Staff","Staff"),
                ("Dagger","Dagger"))

MISC_CHOICES=(("Ring","Ring"),
              ("Amulet","Amulet"),
              ("Missile","Missile"),
              ("Potion","Potion"),
              ("Magic Artifact","Magic Artifact"))

# end definitions


class CharForm(forms.Form):
    type = forms.ChoiceField(choices=users)
    username = forms.CharField(max_length=100, help_text="-Name your epic character !")
    password = forms.CharField(max_length=100, help_text="-Lock the keys to his might !", widget=forms.PasswordInput)
    email = forms.CharField(max_length=100, help_text=" - Give us the name of his messenger pigeon !")


class CharDescForm(forms.Form):
    race = forms.ModelChoiceField(queryset=Race.objects.all(), help_text="Choose your race young one !")
    story = forms.CharField(max_length=500, help_text="Describe how your epic hero becase what hee is now.")
    height = forms.CharField(max_length=10, help_text="How high is your hero ?")
    eyes = forms.CharField(max_length=10, help_text="What is the color of the all seeing eyes of your hero ?")
    bulk = forms.CharField(max_length=10, help_text="How strong is your hero ?")

    class Meta:
        model = Character

class ArmorForm(forms.ModelForm):
    type = forms.ChoiceField(choices=ARMOR_CHOICES, help_text="Armor's type:")
    effect = forms.ModelMultipleChoiceField(label="effect", queryset=Effect.objects.all(), help_text="Armor's effect(s):",
                                            widget=forms.CheckboxSelectMultiple, required=False)
    name = forms.CharField(help_text="Armor's name:")
    defence = forms.IntegerField(help_text="Armor's defence:")
    weight = forms.IntegerField(help_text="Armor's weight:")
    attack = forms.ModelChoiceField(queryset=Formula.objects.all(), help_text="Armor's formula")
    class Meta:
        model = Item
        fields = ("name", "type", "attack", "effect", "defence", "weight")


class WeaponForm(forms.ModelForm):
    type = forms.ChoiceField(choices=WEAPON_CHOICES, help_text="Weapon's type:")
    effect = forms.ModelMultipleChoiceField(label="effect", queryset=Effect.objects.all(), help_text="Weapon's effect(s):",
                                            widget=forms.CheckboxSelectMultiple, required=False)
    name = forms.CharField(help_text="Weapon's name:")
    ap = forms.IntegerField(help_text="Weapon's attack points:")
    attack = forms.ModelChoiceField(queryset=Formula.objects.all(), help_text="Weapon's formula:")
    weight = forms.IntegerField(help_text="Weapon's weight:")
    class Meta:
        model = Item
        fields = ("name", "type", "ap", "attack", "effect", "weight")

class MiscForm(forms.ModelForm):
    type = forms.ChoiceField(choices=MISC_CHOICES, help_text="Item's type:")
    effect = forms.ModelMultipleChoiceField(label="effect", queryset=Effect.objects.all(), help_text="Item's effect(s):",
                                             widget=forms.CheckboxSelectMultiple, required=False)
    name = forms.CharField(help_text="Item's name:")
    weight = forms.IntegerField(help_text="Item's weight:")
    attack = forms.ModelChoiceField(queryset=Formula.objects.all(), help_text="Item's formula")
    class Meta:
        model = Item
        fields = ("name", "type", "attack", "effect", "weight")


