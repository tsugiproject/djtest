from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import requests

from django.views import View

from tsugi.LTIX_classes import *

from . import tsugi_keys

import jwt, json

# Create your views here.

# pip install PyJWT
# pip install cryptography

def launch(request) :
    encoded = request.POST.get('JWT')
    # print(encoded)
    public_key = tsugi_keys.public_key
    lti_launch = jwt.decode(encoded, public_key, algorithms=['RS256'])
    # print(lti_launch)
    request.session['lti_launch'] = lti_launch
    return redirect(reverse_lazy('grade'))

class GradeView(View):  # Reusable bit...

    def get(self, request) :
        launch = TsugiLaunch(tsugi_keys, request)
        print(launch.user.displayname)

        js = json.dumps(launch.lti_launch, indent=4)

        retval = "<pre>\n"+js+"\n</pre>\n"
        context = {'lti_launch' : js, 'launch': launch}
        return render(request, 'launch/main.html', context)

    def post(self, request) :
        launch = TsugiLaunch(tsugi_keys, request)
        grade = float(request.POST.get('grade'))
        comment = request.POST.get('comment')
        # print(grade, comment)
        retval = launch.result.setGrade(grade, comment)
        print('setGrade returns',retval)

        context = {'retval' : retval}
        return render(request, 'launch/graderesult.html', context)


