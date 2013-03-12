# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from character.forms import CharForm, CharDescForm, ArmorForm, WeaponForm, MiscForm, Stats
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from character.models import Character, Race, Item, Log, Ability
from system.models import Skill
from facade.functions import setStats, writeToLog, setEffects
from facade.comfunc import formulaResult, dice
from gm.models import GM


def register(request):
    """
    Register the character (base information -> username, pass, mail)
    """
    context = RequestContext(request)
    register = False
    if request.method == 'POST':
        uniform = CharForm(data=request.POST)
        if uniform.is_valid():
            if uniform.cleaned_data['type'] == 'h':
                if Character.objects.filter(username=uniform.cleaned_data['username']).count() <= 0:
                    # create Hero
                    c = Character()
                    c.username = uniform.cleaned_data['username']
                    c.set_password(uniform.cleaned_data['password'])
                    c.email = uniform.cleaned_data['email']

                    r = Race.objects.all()[0]
                    c.race = r

                    c.save()
                    register = True
                    return HttpResponseRedirect(reverse('character.views.describe', args=(c.id,)))
                else:
                    print "Error ? -> existing user"
            else:
                if Character.objects.filter(username=uniform.cleaned_data['username']).count() <= 0:
                    # create GM -> gm->User
                    g = GM()
                    g.username = uniform.cleaned_data['username']
                    g.set_password(uniform.cleaned_data['password'])
                    g.email = uniform.cleaned_data['email']
                    g.save()
                    register = True
                    return render_to_response('system/main.html', {'master': g, 'reg': register}, context)
                else:
                    print "Error existing gm"
        else:
            print uniform.errors
    else:
        uniform = CharForm()

    return render_to_response('register/register.html', {'uniform': uniform, 'registered': register}, context)


def describe(request, u_id):
    """
    Setting the character race and bonus information
    """
    context = RequestContext(request)
    if request.method == 'POST':
        descform = CharDescForm(data=request.POST)
        if descform.is_valid():
            u = Character.objects.get(pk=u_id)
            u.race = descform.cleaned_data['race']
            u.save()
            # Create log
            l = Log()
            l.text = ""
            l.owner = u
            l.save()
            # set stats
            setStats(u)
            return HttpResponseRedirect(reverse('system.views.main', args=()))
        else:
            print descform.errors
    else:
        descform = CharDescForm()

    return render_to_response('register/char/describe.html', {'descform': descform}, context)

def createArmor(request):
    context = RequestContext(request)
    if request.method == 'POST':
        armorForm = ArmorForm(data=request.POST)
        if armorForm.is_valid():
            armor = Item()
            armor.name = armorForm.cleaned_data['name']
            armor.weight = armorForm.cleaned_data['weight']
            armor.defence = armorForm.cleaned_data['defence']
            armor.type = armorForm.cleaned_data['type']
            armor.attack = armorForm.cleaned_data['attack']
            armor.save()
            armor.effect = armorForm.cleaned_data['effect']
            armor.save()
            return HttpResponseRedirect(reverse('createArmor'))
        else:
            print armorForm.errors
    else:
        armorForm = ArmorForm()

    return render_to_response('character/create/armor.html', {'armorForm': armorForm}, context)

def createWeapon(request):
    context = RequestContext(request)
    if request.method == 'POST':
        weaponForm = WeaponForm(data=request.POST)
        if weaponForm.is_valid():
            weapon = Item()
            weapon.name = weaponForm.cleaned_data['name']
            weapon.weight = weaponForm.cleaned_data['weight']
            weapon.type = weaponForm.cleaned_data['type']
            weapon.ap = weaponForm.cleaned_data['ap']
            weapon.attack = weaponForm.cleaned_data['attack']
            weapon.save()
            weapon.effect = weaponForm.cleaned_data['effect']
            weapon.save()
            return HttpResponseRedirect(reverse('createWeapon'))
        else:
            print weaponForm.errors
    else:
        weaponForm = WeaponForm()

    return render_to_response('character/create/weapon.html', {'weaponForm': weaponForm}, context)


def createMisc(request):
    context = RequestContext(request)
    if request.method == 'POST':
        miscForm = MiscForm(data=request.POST)
        print "test"
        if miscForm.is_valid():
            misc = Item()
            misc.name = miscForm.cleaned_data['name']
            misc.weight = miscForm.cleaned_data['weight']
            misc.type = miscForm.cleaned_data['type']
            misc.attack = miscForm.cleaned_data['attack']
            misc.save()
            misc.effect = miscForm.cleaned_data['effect']
            misc.save()
            return HttpResponseRedirect(reverse('createMisc'))
        else:
            print miscForm.errors
    else:
        miscForm = MiscForm()

    return render_to_response('character/create/misc.html', {'miscForm': miscForm}, context)


def action(request):
    print "Test action"
    type = request.POST.get('typeid', False)
    print type
    character = Character.objects.get(pk=request.user.id)
    setEffects(character)
    if type == '0':
        action = request.POST.get('actid', False)
        calc = Ability.objects.get(name=action)
        final = formulaResult(calc.formula.formula, character) + dice(3)
        result = character.username+ " is using " + str(action) + " with rate of " + str(final) + "</br>"
    elif type == '1':
        action = request.POST.get('actid', False)
        skil = Skill.objects.get(pk=action)
        print skil.formula.formula
        calc = formulaResult(skil.formula.formula, character) + dice(3)
        result = character.username + " is using " + str(skil) + " with rate of " + str(calc) + "</br>"

    writeToLog(character, result)

    return HttpResponse()


def refreshStats(request):
    choice = request.POST.get('actid', False)
    if choice == '0':
        character = Character.objects.get(pk=request.user.id)
        s = Stats.objects.get(character=character)
        result = ""
        s.hpCur-=1
        s.save()
        result += character.username + "," + str(s.xp / 1000) + "," + str(s.hpCur) + "," + str(s.manaCur) + \
                  "," + str(s.xp) + "," + str(s.getAp()) + "," + str(s.sp) + "," + str(s.getHP()) + \
                  "," + str(s.getMana()) + "," + str(s.ap)
    elif choice == '1':
        character = Character.objects.get(pk=request.user.id)
        s = Stats.objects.get(character=character)
        result = ""
        s.hpCur = s.getHP()
        s.manaCur = s.getMana()
        s.apMod = 0
        s.save()
        result += character.username + "," + str(s.xp / 1000) + "," + str(s.hpCur) + "," + str(s.manaCur) + \
                  "," + str(s.xp) + "," + str(s.getAp()) + "," + str(s.sp) + "," + str(s.getHP()) + \
                  "," + str(s.getMana()) + "," + str(s.ap)


    return HttpResponse(result)
