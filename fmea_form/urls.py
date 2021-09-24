from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fmeareg',views.fmeaProcessRegForm,name='fmea'),
    path('fmeaProcess',views.fmeaProcess,name='fmeaprocess'),
    path('fmView',views.view_process,name="view_fmea"),
    #path('edit/<int:id>', views.edit_process,name="edit_fmea"),
    path('update/<int:id>', views.update_process,name="update_fmea"),    
]