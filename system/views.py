# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

def main(request):
    print "Tva e viewto na maina"
    context = RequestContext(request)
    return render_to_response('system/main.html',context)
