from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.index, name='index'),
    path('resourcetype/', views.resourcetype, name='resourcetype'),
    path('getmeeting/', views.getmeeting, name='getmeeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='details'),

]
