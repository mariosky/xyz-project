# Create your views here.




from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import urllib
import urlparse

import json


def index(request):
    if request.user.is_authenticated():
        return render_to_response('xyz/index.html', {}, context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    HttpResponseRedirect('xyz/index.html')# Redirect to a success page.
                else:
                # Return a 'disabled account' error message
                    return HttpResponse( 'disabled account')

            else:
                return HttpResponse( 'invalid login')
                pass
                # Return an 'invalid login' error message.
        else:
            return render_to_response('xyz/signin.html', {}, context_instance=RequestContext(request))

