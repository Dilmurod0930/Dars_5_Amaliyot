from   django.urls import path
from  .views import main,  kom_list, kom_info,  kom_create, kom_delete, kom_update


urlpatterns = [
    path('', main , name='main'),
    path('kom_list/', kom_list , name='kom_list'),
    path('kom_info/<int:id>/', kom_info , name='kom_info'),
    path('kom_create/', kom_create , name='kom_create'),
    path('kom_delete/<int:id>/', kom_delete , name='kom_delete'),
    path('kom_update/<int:id>/', kom_update , name='kom_update'),
]
