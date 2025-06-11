from   django.urls import path
from  .views import main,  kom_info

urlpatterns = [
    path('', main , name='main'),
    path('kom-info', kom_info, name='kom-info'),
]
