from system.models import *
from character.models import *
from gm.models import *
from random import randint
from django.contrib.auth.models import User, UserManager
print "Deleting old data..."
Skill.objects.all().delete()
Profession.objects.all().delete()
Inventory.objects.all().delete()
Item.objects.all().delete()
Character.objects.all().delete()
Race.objects.all().delete()
Stats.objects.all().delete()
GM.objects.all().delete()
Quest.objects.all().delete()

print "Creating Formulas..."
f = Formula(name="sex",formula="sex")
f.save()
f = Formula(name="Swimming",formula="str 2 /")
f.save()
f = Formula(name="Climbing",formula="str 2 /")
f.save()
f = Formula(name="Riding",formula="agi 2 /")
f.save()
f = Formula(name="Sneaking",formula="agi dex + 2 /")
f.save()
f = Formula(name="Jump",formula="str 0 +")
f.save()
f = Formula(name="Charm",formula="beauty int + 2 /")
f.save()
f = Formula(name="Wits",formula="dex 2 / speed 2 / +")
f.save()
f = Formula(name="BaseDefence",formula="lvl 2 / agi +")
f.save()

print "Creating Effects..."
e1 = Effect(name='Drunk',effect="-3 dex")
e1.save()
e2 = Effect(name='Elven Knowledge',effect="+3 dmg to bow")
e2.save()
e3 = Effect(name='Stone skin',effect=" +4 str, -2 agi")
e3.save()
e4 = Effect(name='Poison',effect=" -10 hp")
e4.save()

print "Creating Skills..."
skill1 = Skill(name="Rapid Fire",effect=" -1 ap, -1 dmg d",lvl=3,isPassive=False)
skill2 = Skill(name="Precision Shot",effect="+2 ap , +1 dmg d",lvl=6,isPassive=False)
skill3 = Skill(name="Shout",effect="+4 sre",lvl=2,isPassive=False)
skill4 = Skill(name = "Keen eye",effect="+3 agi",lvl=3,isPassive=True)
skill1.save()
skill2.save()
skill3.save()
skill4.save()

print "Creating Professions..."
prof1 = Profession(name="Archery",lvl=4)
prof1.save()    # save before creating a many to many relationship
prof1.skills.add(skill1)
prof1.save()
prof1.skills.add(skill2)
prof1.save()
prof1.skills.add(skill4)
prof1.save()

prof2 = Profession(name="Warrior",lvl=4)
prof2.save()
prof2.skills.add(skill3)
prof2.save()

print "Creating Races..."
race1 = Race(name="Dwarf",str=7,strMax=15,agi=4,agiMax=16,int=6,intMax=18,dex=5,dexMax=17,vitality=3,speed=15)
race2 = Race(name="Elf",str=5,strMax=16,agi=6,agiMax=18,int=6,intMax=19,dex=6,dexMax=19,vitality=1,speed=18)
race1.save()
race2.save()

print "Creating Characters..."
c1 = Character(username="Dulan",race=race1)
c1.sp = 0
c2 = Character(username="Enferia",race=race2)
c2.sp =0
c1.save()
c2.save()  # save before creating a many to many relationship
c1.profession.add(prof1)
c2.profession.add(prof2)
c1.save()
c2.save()


print "Creating Stats..."
s1 = Stats(xp=0,character=c1,str=race1.str,strMax=race1.strMax,agi=race1.agi,agiMax=race1.agiMax,int=race1.int,intMax=race1.intMax,dex=race1.dex,dexMax=race1.dexMax,vitality=race1.vitality,speed=race1.speed,beauty=randint(1,18))
s2 = Stats(xp=0,character=c2,str=race2.str,strMax=race2.strMax,agi=race2.agi,agiMax=race2.agiMax,int=race2.int,intMax=race2.intMax,dex=race2.dex,dexMax=race2.dexMax,vitality=race2.vitality,speed=race2.speed,beauty=randint(1,18))
s1.save()
s2.save()

print "Creating Items..."
m1 = Item(name="mana potion",type="Potion",weight=1,attack=f)
m1.save()
m2 = Item(name="health potion",type="Potion",weight=1,attack=f)
m2.save()
a1 = Item(name="Cloth",type="Chest",defence=0,weight=3,attack=f)
a1.save()
a2 = Item(name="chain mail",type="Chest",defence=10,weight=20,attack=f)
a2.save()
w1 = Item(name="sword",type="Sword",dmg=3,weight=4,ap=5,attack=f)
w1.save()
w2 = Item(name="bow",type="Bow",dmg=3,weight=4,ap=7,attack=f)
w2.save()

print "Creating Inventory..."
for i in Item.objects.all():
    iv = Inventory(owner=c1,item=i,durability=20)
    iv.save()
    iv = Inventory(owner=c2,item=i,durability=20)
    iv.save()

print "Creating GMs..."
gm1 = GM(username="Entaria")
gm1.save()
gm2 = GM(username="TerrorRealm")
gm2.save()

print "Creating Quests"
q1 = Quest(gm=gm1,title="The Merchant Wish",snippet="You will receive letters from time to time that will explain your tasks",xp=400)
q2 = Quest(gm=gm1,title="Wolf Problem",snippet="There are packs of wolves arround the trade routs, kill them",xp=200)
q3 = Quest(gm=gm2,title="Kill John",snippet="Find who John is and kill him",xp=1400)
q1.save()
q1.save()
q3.save()
