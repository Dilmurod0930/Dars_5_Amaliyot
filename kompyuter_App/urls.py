from   django.urls import path
from  .models import main

urlpatterns = [
    path('', main , name='main'),

]
