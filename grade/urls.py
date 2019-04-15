
from django.urls import path
from . import views
from django.views.generic import TemplateView
from tsugi.views import LaunchView

urlpatterns = [
    path('', LaunchView.as_view(), {'success_url' : 'grade'} ),
    path('grade', views.GradeView.as_view(), name='grade' ),
]

