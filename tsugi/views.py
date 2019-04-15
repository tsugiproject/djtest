from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

import requests

from django.views import View

from tsugi.LTIX_classes import *

from grade import tsugi_keys

import jwt, json

# Create your views here.

# pip install PyJWT
# pip install cryptography

class LaunchView(View) :
    def post(self, request, success_url) :
        print('success_url', success_url)
        encoded = request.POST.get('JWT')
        # print(encoded)
        public_key = tsugi_keys.public_key
        lti_launch = jwt.decode(encoded, public_key, algorithms=['RS256'])
        # print(lti_launch)
        request.session['lti_launch'] = lti_launch
        return redirect(reverse_lazy(success_url))

