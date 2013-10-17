# Create your views here.




from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from models import Painting, Generation

import urllib
import urlparse

import json


def index(request):
    print "index"
    if request.user.is_authenticated():
        return HttpResponseRedirect('last_generation')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse( 'nice login')
                    #print "login"
                    return HttpResponseRedirect('last_generation')# Redirect to a success page.
                else:
                # Return a 'disabled account' error message
                    return HttpResponse( 'disabled account')

            else:
                return HttpResponse( 'invalid login')

                # Return an 'invalid login' error message.
        else:
            return render_to_response('xyz/signin.html', {}, context_instance=RequestContext(request))


def generation(request,gen=0):
    if request.user.is_authenticated():
        next_gen = Generation.objects.filter(next_generation=True)[0]
        current_gen = Generation.objects.filter(generation_number=next_gen.generation_number-1)[0]
        paintings = gen.painting_set.all()




        return render_to_response('xyz/generation.html', {'next_gen':next_gen,"current_gen" : current_gen,
                                                          "paintings":paintings}, context_instance=RequestContext(request))
    else:
        return render_to_response('xyz/signin.html', {}, context_instance=RequestContext(request))


def upload(request):
     return render_to_response('xyz/upload.html', {}, context_instance=RequestContext(request))




@csrf_exempt
def upload_minimal(request):
    if request.method == 'POST':
            print request.POST[u'parents']
            #print 'Raw Data___: "%s"' % request.body
            print request.FILES.keys()
            print request.FILES["fileToUpload"]
            print request.POST[u'generation']


            gen = Painting.objects.get(pk=int(request.POST[u'generation']))

            painting = Painting(title=request.POST[u'title'], author=request.user, summary=request.POST[u'summary'],
                                image=request.FILES["fileToUpload"],generation=gen)
            painting.save()
            for _id in request.POST[u'parents'].split(','):
                painting.parents.add(Painting.objects.get(pk=_id))
                print "o"
            print painting.parents.all()

            #json_data = json.loads(request.body)

            #id     = json_data["id"]
            data = json.dumps({"result" : "saved","error": None, "id": 12})
            return HttpResponse(data, mimetype='application/json')
    else:
        data = json.dumps(data = json.dumps({"result" : "saved","error": None, "id": id}))
        return HttpResponse(data, mimetype='application/json')




