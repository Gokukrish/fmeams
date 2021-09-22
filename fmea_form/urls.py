from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fmeareg',views.fmeaProcessRegForm,name='fmea'),
    path('fmeaProcess',views.fmeaProcess,name='fmeaprocess'),
    path('fmView',views.view_process,name="view_fmea")
]