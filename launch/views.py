from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import tsugi_keys

import jwt, json

# Create your views here.

# pip install PyJWT
# pip install cryptography

def launch(request) :
    encoded = request.POST.get('JWT');
    print(encoded)

    public_key = tsugi_keys.public_key;
    decoded = jwt.decode(encoded, public_key, algorithms=['RS256'])
    print(decoded)
    request.session['decoded'] = decoded
    return redirect(reverse_lazy('grade'))


def grade(request):

    decoded = request.session.get('decoded') 
    js = json.dumps(decoded, indent=4)

    retval = "<pre>\n"+js+"\n</pre>\n";
    context = {'debug_decoded' : js}
    return render(request, 'launch/main.html', context)

