from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django_tsugi.mixins import TsugiMixin

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
        <input type="submit" value="Form 1">
        </form>
        <form method="post">
        <input type="submit" value="Form 2">
        </form>
        </p>
        <a href="test">test</a></p>
        <p><a href="""+'"'+request.path+'"'+""">"""+request.path+"""</a></p>
        <a href="https://www.dr-chuck.com/">External site</a></p>
        </body></html>"""
        return HttpResponse(response)

    def post(self, request) :
        print('I am post')
        return HttpResponseRedirect(request.path)
