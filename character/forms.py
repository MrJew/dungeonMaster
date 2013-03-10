__author__ = 'ivaylo'
from character.models import *
from django import forms


# Define some stuff here
users = (('g', 'gm'), ('h', 'hero'))

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