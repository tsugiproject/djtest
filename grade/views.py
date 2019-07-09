from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from django.conf import settings


from django_tsugi.mixins import TsugiMixin

from jwcrypto import jwk
import urllib.request, urllib.parse, urllib.error


class GradeView(TsugiMixin, View):

    def get(self, request) :
        context = {'tsugi': request.tsugi}
        return render(request, 'grade/main.html', context)

    def post(self, request) :
        grade = float(request.POST.get('grade'))
        comment = request.POST.get('comment')

        retval = request.tsugi.result.gradeSend(grade, comment)
        context = {'tsugi': request.tsugi, 'retval' : retval}
        return render(request, 'grade/done.html', context)

class TestView(View) :
    def get(self, request) :
        print('YADA', settings.TSUGI_KEYSET);
        dat = urllib.request.urlopen(settings.TSUGI_KEYSET).read();
        print(dat)

        # https://github.com/latchset/jwcrypto/blob/master/jwcrypto/tests.py
        # https://jwcrypto.readthedocs.io/en/latest/jwk.html#classes
        ks = jwk.JWKSet()
        ks.import_keyset(dat);
        print(ks)
        kid = 'e98e2ba54b485cf570d197a33ad56d329eff07d18babbb4ef24334bd70045eab'
        k1 = ks.get_key(kid)
        print(k1)
        pub = jwk.JWK.export_to_pem(k1)
        print(pub)
        response = """
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)

