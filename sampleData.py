from system.models import *
from character.models import *
from gm.models import *
from random import randint
from django.contrib.auth.models import User, UserManager
print "Deleting old data..."
Skill.objects.all().delete()
Profession.objects.all().delete()
SetProfessions.objects.all().delete()
Inventory.objects.all().delete()
Item.objects.all().delete()
Character.objects.all().delete()
Race.objects.all().delete()
Stats.objects.all().delete()
GM.objects.all().delete()
Quest.objects.all().delete()
Ability.objects.all().delete()
Effect.objects.all().delete()

print "Creating Formulas..."
sw = Formula(name="Swimming",formula="str 2 /")
sw.save()
cl = Formula(name="Climbing",formula="str 2 /")
cl.save()
ri = Formula(name="Riding",formula="agi 2 /")
ri.save()
sn = Formula(name="Sneaking",formula="agi dex + 2 /")
sn.save()
ju = Formula(name="Jump",formula="str 0 +")
ju.save()
be = Formula(name="Charm",formula="beauty int + 2 /")
be.save()
wi = Formula(name="Wits",formula="dex 2 / speed 2 / +")
wi.save()
bd = Formula(name="BaseDefence",formula="lvl 2 / agi +")
bd.save()
st = Formula(name="Stability",formula="lvl 2 / agi +")
st.save()
ap = Formula(name="Action Points",formula="speed agi + 2 /")
ap.save()
empty = Formula(name="empty",formula='0 0 +')
empty.save()


print "Creating Abilities..."
a = Ability(name=st.name,formula=st,level=0)
a.save()
a = Ability(name=bd.name,formula=bd,level=0)
a.save()
a = Ability(name=wi.name,formula=wi,level=0)
a.save()
a = Ability(name=be.name,formula=be,level=0)
a.save()
a = Ability(name=ju.name,formula=ju,level=0)
a.save()
a = Ability(name=sn.name,formula=sn,level=0)
a.save()
a = Ability(name=ri.name,formula=ri,level=0)
a.save()
a = Ability(name=cl.name,formula=cl,level=0)
a.save()
a = Ability(name=sw.name,formula=sw,level=0)
a.save()


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
skill1 = Skill(name="Rapid Fire",lvl=3,isPassive=False,formula=empty)
skill2 = Skill(name="Precision Shot",lvl=6,isPassive=False,formula=empty)
skill3 = Skill(name="Shout",lvl=2,isPassive=False,formula=empty)
skill4 = Skill(name = "Keen eye",lvl=3,isPassive=True,formula=empty)
skill5 = Skill(name = "Poison Resistance",lvl=2,isPassive=True,formula=empty)
skill6 = Skill(name = "Brewing",lvl=0,isPassive=False,formula=empty)
skill1.save()
skill2.save()
skill3.save()
skill4.save()
skill5.save()
skill6.save()
skill1.effect.add(e1)
skill2.effect.add(e2)
skill3.effect.add(e3)
skill4.effect.add(e4)
skill5.effect.add(e1)
skill6.effect.add(e1)
skill1.save()
skill2.save()
skill3.save()
skill4.save()
skill5.save()
skill6.save()

print "Creating Professions..."
prof1 = Profession(name="Archery")
prof1.save()    # save before creating a many to many relationship
prof1.skills.add(skill1)
prof1.save()
prof1.skills.add(skill2)
prof1.save()
prof1.skills.add(skill4)
prof1.save()

prof2 = Profession(name="Warrior")
prof2.save()
prof2.skills.add(skill3)
prof2.save()

prof3 = Profession(name="Alchemy")
prof3.save()
prof3.skills.add(skill5)
prof3.skills.add(skill6)
prof3.save()

print "Creating Races..."
race1 = Race(name="Dwarf",hp=23,str=7,strMax=15,agi=4,agiMax=16,int=6,intMax=18,dex=5,dexMax=17,vitality=3,speed=15)
race2 = Race(name="Elf",hp=18,str=5,strMax=16,agi=6,agiMax=18,int=6,intMax=19,dex=6,dexMax=19,vitality=1,speed=18)
race1.save()
race2.save()

print "Creating Characters..."
c1 = Character(username="Dulan",email="dulan@example.com",race=race1)
c1.set_password("123")
c1.sp = 0
c2 = Character(username="Enferia",email="enferia@example.com",race=race2)
c2.sp = 0
c2.set_password("123")
c1.save()
c2.save()  # save before creating a many to many relationship

print "Creating Logs..."
l1 = Log(owner=c1,text='')
l2 = Log(owner=c2,text='')
l1.save()
l2.save()

print "Creating SetProffessions..."
sp = SetProfessions(owner=c1,profession=prof1,level=5)
sp.save()
sp = SetProfessions(owner=c1,profession=prof3,level=8)
sp.save()
sp = SetProfessions(owner=c2,profession=prof2,level=6)
sp.save()


print "Creating Stats..."
s1 = Stats(sp=0,xp=0,hp=race1.hp,character=c1,str=race1.str,strMax=race1.strMax,agi=race1.agi,agiMax=race1.agiMax,int=race1.int,intMax=race1.intMax,dex=race1.dex,dexMax=race1.dexMax,vitality=race1.vitality,speed=race1.speed,beauty=randint(1,18))
s2 = Stats(sp=0,xp=0,hp=race2.hp,character=c2,str=race2.str,strMax=race2.strMax,agi=race2.agi,agiMax=race2.agiMax,int=race2.int,intMax=race2.intMax,dex=race2.dex,dexMax=race2.dexMax,vitality=race2.vitality,speed=race2.speed,beauty=randint(1,18))
s1.save()
s2.save()

print "Creating Items..."
m1 = Item(name="mana potion",type="Potion",weight=1,attack=sw)
m1.save()
m2 = Item(name="health potion",type="Potion",weight=1,attack=sw)
m2.save()
a1 = Item(name="Cloth",type="Chest",defence=0,weight=3,attack=sw)
a1.save()
a2 = Item(name="chain mail",type="Chest",defence=10,weight=20,attack=sw)
a2.save()
w1 = Item(name="sword",type="Sword",dmg=3,weight=4,ap=5,attack=sw)
w1.save()
w2 = Item(name="bow",type="Bow",dmg=3,weight=4,ap=7,attack=sw)
w2.save()

print "Creating Inventory..."

iv = Inventory(owner=c1,item=m1,durability=20,type='M',equiped=True)
iv.save()
iv = Inventory(owner=c1,item=m2,durability=20,type='M',equiped=True)
iv.save()
iv = Inventory(owner=c1,item=a1,durability=20,type='A',equiped=True)
iv.save()
iv = Inventory(owner=c1,item=a2,durability=20,type='A',equiped=True)
iv.save()
iv = Inventory(owner=c1,item=w1,durability=20,type='W',equiped=True)
iv.save()
iv = Inventory(owner=c2,item=m2,durability=20,type='M',equiped=True)
iv.save()
iv = Inventory(owner=c2,item=a2,durability=20,type='A',equiped=True)
iv.save()
iv = Inventory(owner=c2,item=w2,durability=20,type='W',equiped=True)
iv.save()

print "Creating GMs..."
gm1 = GM(username="Entaria")
gm1.set_password("123")
gm1.save()
gm2 = GM(username="TerrorRealm")
gm2.set_password("123")
gm2.save()

print "Creating Quests"
q1 = Quest(gm=gm1,title="The Merchant Wish",snippet="You will receive letters from time to time that will explain your tasks",xp=400)
q2 = Quest(gm=gm1,title="Wolf Problem",snippet="There are packs of wolves arround the trade routs, kill them",xp=200)
q3 = Quest(gm=gm2,title="Kill John",snippet="Find who John is and kill him",xp=1400)
q1.save()
q2.save()
q3.save()
q1.players.add(c1)
q1.players.add(c2)
q2.players.add(c1)
q2.players.add(c2)
q3.players.add(c1)
q1.save()
q1.save()
q3.save()