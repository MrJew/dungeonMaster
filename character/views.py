# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from character.forms import CharForm


def register(request):
    context = RequestContext(request)
    register = False
    if request.method == 'POST':
        uniform = CharForm(data=request.POST)
        if uniform.is_valid():
            # do the register dance#
            print("Do some regsistering !")
        else:
            print uniform.errors
    else:
        uniform = CharForm()

    return render_to_response('register/register.html', {'uniform': uniform, 'registered': register}, context)
