
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.launch ),
    path('grade', views.GradeView.as_view(), name='grade' ),
]

