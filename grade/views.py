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
    def get(self, request):
        request.session['bob'] = request.session.get('bob', 0) + 1;
        response = """<html><body><p>Bob="""+str(request.session['bob'])+"""</p>
        <p>
        <form method="post">
        <input type="submit" value="Click">
        </form>
        <form method="post">
        <input type="submit" value="Click 2">
        </form>
        </p>
        <p>This sample code is available at
        <a href="""+'"'+request.path+'"'+""">click</a></p>
        <a href="https://www.dr-chuck.com/">Chuck</a></p>
        <a href="test">click 2</a></p>
        </body></html>"""
        return HttpResponse(response)

    def post(self, request) :
        print('I am post')
        return self.get(request)
