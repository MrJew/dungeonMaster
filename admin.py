from django.contrib import admin
from character.models import *
from gm.models import *
from character import *
from system.models import *

admin.site.register(GM)
admin.site.register(Character)
admin.site.register(Race)