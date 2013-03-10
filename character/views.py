# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from character.forms import CharForm, CharDescForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from character.models import Character, Race
from gm.models import GM


def register(request):
    context = RequestContext(request)
    register = False
    if request.method == 'POST':
        uniform = CharForm(data=request.POST)
        if uniform.is_valid():
            if uniform.cleaned_data['type'] == 'h':
                # create Hero
                c = Character()
                c.username = uniform.cleaned_data['username']
                c.set_password(uniform.cleaned_data['password'])
                c.email = uniform.cleaned_data['email']

                r = Race.objects.all()[0]
                c.race = r

                c.save()
                #return render_to_response('register/Char/describe.html', {'char': c, 'reg': register}, context)
                register = True
                return HttpResponseRedirect(reverse('character.views.describe', args=(c.id,)))
            else:
                # create GM -> gm->User
                g = GM()
                g.username = uniform.cleaned_data['username']
                g.set_password(uniform.cleaned_data['password'])
                g.email = uniform.cleaned_data['email']
                g.save()
                register = True
                return render_to_response('system/main.html', {'master': g, 'reg': register}, context)
        else:
            print uniform.errors
    else:
        uniform = CharForm()

    return render_to_response('register/register.html', {'uniform': uniform, 'registered': register}, context)


def describe(request, u_id):
    context = RequestContext(request)
    if request.method == 'POST':
        descform = CharDescForm(data=request.POST)
        if descform.is_valid():
            u = Character.objects.get(pk=u_id)
            u.race = descform.cleaned_data['race']
            u.save()

            return render_to_response('system/main.html', context)
        else:
            print descform.errors
    else:
        descform = CharDescForm()

    return render_to_response('register/char/describe.html', {'descform': descform}, context)
