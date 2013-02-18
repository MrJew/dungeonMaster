from character.models import *
from gm.models import *
from system.models import *
from django.contrib.auth.models import User, UserManager

prof1 = Profession(name="Archery",lvl=4)
prof2 = Profession(name="Warrior",lvl=4)

skill1 = Skill(name="Rapid Fire",prof=prof1,lvl=3,effect="Attack cost less ap but deal less dmg",isPassive=False)
skill2 = Skill(name="Precision Shot",prof=prof1,lvl=6,effect="Attack costs more ap but deals more dmg",isPassive=False)
skill3 = Skill(name="Shout",prof=prof2,lvl=2,effectt="Gain + 4 strength",isPassive=False)
skill4 = Skill(name = "Keen eye",prof=prof1,lvl=3,effect="gain +5 range attacks",isPassive=True)

race1 = Race(name="Dwarf",str=7,strMax=15,agi=4,agiMax=16,int=6,intMax=18,dex=5,dexMax=17,vitality=3,speed=15)
race2 = Race(name="Elf",str=5,strMax=16,agi=6,agiMax=18,int=6,intMax=19,dex=6,dexMax=19,vitality=1,speed=18)

stats

