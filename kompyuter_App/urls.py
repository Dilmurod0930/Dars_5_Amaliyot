from   django.urls import path
from  .views import main,  kom_list, kom_info,  kom_create

urlpatterns = [
    path('', main , name='main'),
    path('kom_list/', kom_list , name='kom_list'),
    path('kom_info/<int:id>/', kom_info , name='kom_info'),
    path('kom_create/', kom_create , name='kom_create'),
]
