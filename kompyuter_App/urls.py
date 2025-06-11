from   django.urls import path
from  .views import main,  kom_list

urlpatterns = [
    path('', main , name='main'),
    path('kom_list', kom_list , name='kom_list'),
]
