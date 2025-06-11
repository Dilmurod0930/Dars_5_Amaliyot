from  django.urls import path
from  .views import tele_list, tele_info, tele_create ,tele_delete , tele_update

urlpatterns =[
    path('tele_list', tele_list, name='tele_list'),
    path('tele_info/<int:id>', tele_info, name='tele_info'),
    path('tele_create', tele_create, name='tele_create'),
    path('tele_delete/<int:id>', tele_delete, name='tele_delete'),
    path('tele_update/<int:id>', tele_update, name='tele_update'),

]