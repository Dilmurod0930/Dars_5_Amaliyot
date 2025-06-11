from  django.urls import path
from  .views import tele_list

urlpatterns =[
    path('tele_list', tele_list, name='tele_list'),
]