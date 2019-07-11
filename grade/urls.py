
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django_tsugi.views import LaunchView

from django_tsugi.decorators import no_cookies

urlpatterns = [
    path('', no_cookies(views.GradeView.as_view()), name='grade' ),
    path('launch', no_cookies(LaunchView.as_view()), {'success_url' : 'grade'} ),
    path('launch/', no_cookies(LaunchView.as_view()), {'success_url' : 'grade'} ),
    path('test', no_cookies(views.TestView.as_view()) ),
    path('test/', no_cookies(views.TestView.as_view()) ),
]

