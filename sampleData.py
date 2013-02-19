from system.models import *
from character.models import *
from gm.models import *

from django.contrib.auth.models import User, UserManager



skill1 = Skill(name="Rapid Fire",lvl=3,effect="Attack cost less ap but deal less dmg",isPassive=False)
skill2 = Skill(name="Precision Shot",lvl=6,effect="Attack costs more ap but deals more dmg",isPassive=False)
skill3 = Skill(name="Shout",lvl=2,effect="Gain + 4 strength",isPassive=False)
skill4 = Skill(name = "Keen eye",lvl=3,effect="gain +5 range attacks",isPassive=True)
skill1.save()
skill2.save()
skill3.save()
skill4.save()

prof1 = Profession(name="Archery",lvl=4,skills=(skill1,skill2,skill3))
prof2 = Profession(name="Warrior",lvl=4,skills=(skill3))
prof1.save()
prof2.save()

m1 = Misc(name="mana potion")
m1.save()
m2 = Misc(name="health potion")
m2.save()
a1 = Armor(name="Cloth")
a1.save()
a2 = Armor(name="chain mail")
a2.save()
w1 = Weapon(name="sword")
w1.save()
w2 = Weapon(name="bow")
w2.save()

c1 = Character(proffesion=prof1,weapons=w1,misc=m1,armor=a1)
c1.sp = 0
c2 = Character(proffesion=prof2,weapons=w2,misc=m2,armor=a2)
c2.sp =0
c1.save()
c2.save()

race1 = Race(character=c1,name="Dwarf",str=7,strMax=15,agi=4,agiMax=16,int=6,intMax=18,dex=5,dexMax=17,vitality=3,speed=15)
race2 = Race(character=c2,name="Elf",str=5,strMax=16,agi=6,agiMax=18,int=6,intMax=19,dex=6,dexMax=19,vitality=1,speed=18)
race1.save()
race2.save()

s1 = Stats(character=c1,str=race1.str,strMax=race1.strMax,agi=race1.agi,agiMax=race1.agiMax,int=race1.int,intMax=race1.intMax,dex=race1.dex,dexMax=race1.dexMax,vitality=race1.vitality,speed=race1.speed)
s2 = Stats(character=c2,str=race2.str,strMax=race2.strMax,agi=race2.agi,agiMax=race2.agiMax,int=race2.int,intMax=race2.intMax,dex=race2.dex,dexMax=race2.dexMax,vitality=race2.vitality,speed=race2.speed)
s1.save()
s2.save()