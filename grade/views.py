from django.shortcuts import render
from django.views import View

from tsugi.mixins import TsugiMixin

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


