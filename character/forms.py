__author__ = 'ivaylo'
from character.models import *
from django.forms import *


# Define some stuff here
users = (('g', 'gm'), ('h', 'hero'))

# end definitions


class CharForm(forms.Form):
    type = forms.ChoiceField(choices=users)

    class Meta:
        model = Character
        fields = ["username", "email", "password"]
