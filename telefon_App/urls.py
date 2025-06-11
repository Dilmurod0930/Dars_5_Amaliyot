from  django.urls import path
from  .views import tele_info

urlpatterns =[
    path('tele_info', tele_info, name='tele_info'),
]