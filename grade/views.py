from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import requests

from django.views import View

from tsugi.LTIX_classes import *

import json

# Create your views here.

# pip install PyJWT
# pip install cryptography

class GradeView(View):  # Reusable bit...

    def get(self, request) :
        launch = TsugiLaunch(request)

        js = json.dumps(launch.lti_launch, indent=4)
        context = {'lti_launch' : js, 'launch': launch}
        return render(request, 'launch/main.html', context)

    def post(self, request) :
        launch = TsugiLaunch(request)
        grade = float(request.POST.get('grade'))
        comment = request.POST.get('comment')
        # print(grade, comment)
        retval = launch.result.setGrade(grade, comment)
        print('setGrade returns',retval)

        context = {'retval' : retval}
        return render(request, 'launch/graderesult.html', context)


